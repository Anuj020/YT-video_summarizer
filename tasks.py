from crewai import Task
from tools import yt_tool
from agents import blog_writer, blog_researcher

## Research Task
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output= 'A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher
)


writting_task = Task(
    description=(
        "get the info from the youtube channel on the {topic}."
    ),
    expected_output= 'summarize the info from the youtube channel video on the topic {topic} abd create the content for the blog.',
    tools=[yt_tool],
    agent=blog_writer,
    # True - agents work parallel 
    async_execution=False,
    output_file='new-blog-post.md' 
)