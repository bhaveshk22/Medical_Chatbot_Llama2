from flask import Flask, render_template, jsonify, request
from src.helper import download_huggingface_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *

import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


embeddings = download_huggingface_embeddings()

#Initializing the Pinecone
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

index_name="medical-chatbot"

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

knowledge = PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    namespace="default",
    embedding=embeddings
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=knowledge.as_retriever(search_kwargs={'k': 2}),
    # chain_type_qwargs = chain_type_kwargs
    chain_type_kwargs={"prompt": PROMPT}
)


@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)


