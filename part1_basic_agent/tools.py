from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.tools import PythonREPLTool

search = DuckDuckGoSearchRun()
python_tool = PythonREPLTool()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Search the web"
    ),
    Tool(
        name="Python",
        func=python_tool.run,
        description="Execute python code"
    )
]