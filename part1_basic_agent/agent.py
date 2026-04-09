from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools import tools
from memory import get_memory

def create_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Prompt officiel React agent
    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=get_memory(),
        verbose=True
    )

    return agent_executor