from crewai import Agent
from tools import yt_tool
from crewai import LLM
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
API_KEY = os.getenv("OPENAI_API_KEY")

llm = LLM(
    model="openai/gpt-4o",
    api_key=API_KEY,  # Or set OPENAI_API_KEY
    temperature=0.7
)

## create a senior blog content researcher
blog_researcher = Agent(
    role = 'Blog researcher from youtube videos',
    goal = 'get the relevant video content for the topic {topic} from yt channle',
    verbose = True,
    memory = False,
    # backstroy about particular agent
    backstory = (
        "Expert in understanding videos in AI Data science, Machine Learning, and Gen AI and providing suggestion"
    ), 
    tools=[yt_tool],
    llm =llm,
    #  True - transfering work whatever this agent does to someone else
    allow_delegation = True,
)

## Creating a senior blog writer agent with YT tool
blog_writer = Agent(
    role = 'Blog writer',
    goal = 'Narrate compelling tech stories about the video {topic} from YT channle',
    verbose = True,
    memory = False,
    # backstroy about particular agent
    backstory = (
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to ligt in an accessible manner."
    ), 
    tools=[yt_tool],
    llm=llm,
    #  False -  Not transfering work whatever this agent does to someone else
    allow_delegation = False,
)