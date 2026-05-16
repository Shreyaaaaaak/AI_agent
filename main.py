from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import create_react_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGroq(model="llama-3.3-70b-versatile")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = SystemMessage(content="""
You are a research assistant that will help in generating a research paper.
Answer the user query and use necessary tools.
Do NOT call save_tool — just return the final answer.
Wrap the output in this format and provide no other text:
""" + parser.get_format_instructions())

agent = create_react_agent(
    model=llm,
    tools=[search_tool, wiki_tool, save_tool],
    prompt=system_prompt
)

query = input("What can I help you research? ")
raw_response = agent.invoke({"messages": [("human", query)]})

try:
    output = raw_response["messages"][-1].content
    structured_response = parser.parse(output)
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)