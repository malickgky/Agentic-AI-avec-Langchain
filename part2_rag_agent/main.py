from vector_store import create_vector_store
from rag_agent import create_rag_agent

docs = [
    "LangChain is a framework for building LLM apps",
    "RAG combines retrieval and generation"
]

vectorstore = create_vector_store(docs)
rag = create_rag_agent(vectorstore)

query = input("Question: ")
print(rag.run(query))