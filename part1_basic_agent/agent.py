from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from tools import tools
from memory import get_memory

def create_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    agent = initialize_agent(
        tools,
        llm,
        agent="chat-conversational-react-description",
        memory=get_memory(),
        verbose=True
    )
    return agent