from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def create_rag_agent(vectorstore):
    retriever = vectorstore.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        retriever=retriever
    )

    return qa