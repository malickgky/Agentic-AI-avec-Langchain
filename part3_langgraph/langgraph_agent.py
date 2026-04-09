from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI

def agent_node(state):
    llm = ChatOpenAI()
    response = llm.invoke(state["input"])
    return {"output": response.content}

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")

    return graph.compile()