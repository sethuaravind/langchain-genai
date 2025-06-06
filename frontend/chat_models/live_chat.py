from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# from dotenv import load_dotenv


# load_dotenv()

# prompt = ChatPromptTemplate.from_messages([
#     ('system', 'you are a useful assistant'),
#     ('human', "'{input}'"),
#     ('placeholder'), "'{agent_scratchpad}'"
# ])


def live_chat(query):
    prompt = hub.pull("hwchase17/react")
    tools = [TavilySearchResults()]
    llm = ChatOpenAI(temperature=0)
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    res = agent_executor.invoke({'input': query})

    return res['output']