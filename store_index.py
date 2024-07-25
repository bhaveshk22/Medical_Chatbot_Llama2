from src.helper import load_pdf, download_huggingface_embeddings, text_split
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


extracted_data = load_pdf('data')
text_chunks = text_split(extracted_data)
embeddings = download_huggingface_embeddings()


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name="chatbot",
    embedding=embeddings, 
    namespace="default" 
)