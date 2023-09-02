import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv

load_dotenv()

def create_vector_db():
  pdfs = PyPDFDirectoryLoader('./')
  data = pdfs.load()

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=100
  )

  texts = text_splitter.split_documents(data)
  # print(texts)

  embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv('OPENAI_API_KEY')
  )

  pinecone_api_key=os.getenv('PINECONE_API_KEY')
  pinecone_env_key=os.getenv('PINECONE_ENV_KEY')

  pinecone.init(
    api_key=pinecone_api_key, 
    environment=pinecone_env_key
  )
  index_name = "storage"

  vectordb = Pinecone.from_documents(texts, embeddings, index_name=index_name)

  return vectordb