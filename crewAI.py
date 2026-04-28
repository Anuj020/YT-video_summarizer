from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,writting_task


## Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,writting_task],
    process= Process.sequential,
    memory=False,
    embedder=None,
    cache=True,
    max_rpm=100,
    share_crew=True
)


## start the task execution process with enhanced feedbacl
result = crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data science'})
print(result)