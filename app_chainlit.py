from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl
from src.prompt import *
from langchain_pinecone import PineconeVectorStore

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

#Retrieval QA Chain
def retrieval_qa_chain(llm, PROMPT, knowledge):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type="stuff",
                                           retriever=knowledge.as_retriever(search_kwargs={'k': 2}),
                                           # chain_type_qwargs = chain_type_kwargs
                                           chain_type_kwargs={"prompt": PROMPT}
                                           )
    return qa_chain

#Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm=CTransformers(
        model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        config={'max_new_tokens':512, 'temperature':0.8})
    return llm

#QA Model Function
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    knowledge = PineconeVectorStore.from_existing_index(
        index_name="medical-chatbot",
        namespace="default",
        embedding=embeddings
        )
    
    llm = load_llm()
    qa_prompt = PROMPT
    qa = retrieval_qa_chain(llm, qa_prompt, knowledge)

    return qa



#output function
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

#chainlit code
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to Medical Bot. What is your query?"
    await msg.update()

    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")
    if chain is None:
        await cl.Message(content="Error: QA chain not initialized.").send()
        return

    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["result"]
    # sources = res["source_documents"]

    # if sources:
    #     answer += f"\nSources:" + str(sources)
    # else:
    #     answer += "\nNo sources found"

    await cl.Message(content=answer).send()