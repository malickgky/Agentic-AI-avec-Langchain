from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(texts):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts, embeddings)