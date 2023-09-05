from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
import os
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from dotenv import find_dotenv, load_dotenv

OPENAI_API_KEY = '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'

# Load environment variables from .env file
load_dotenv(find_dotenv())

search = SerpAPIWrapper()
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

agent_chain.run(input="who is the current governor of Tennessee")