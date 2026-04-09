from langgraph_agent import build_graph

graph = build_graph()

result = graph.invoke({"input": "Explain RAG"})
print(result)