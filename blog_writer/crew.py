from crewai import Crew,Process
import os
from tasks import research_task,write_task
from agents import news_researcher,news_writer


os.environ["LANGCHAIN_PROJECT"] = "crewai"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
)

result=crew.kickoff(inputs={'topic':'AI in war'})
print(result)
