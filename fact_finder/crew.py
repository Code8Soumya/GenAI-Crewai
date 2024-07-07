import os
from crewai import Crew, Process
from tasks import fact_finding_task
from agents import fact_finder_agent
from tools import trending_topic_finder
from pyairtable import Api
import time
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_PROJECT"] = "fact-finder"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

api = Api(os.environ['AIRTABLE_API_KEY'])
table = api.table('appvGMvGGmDBicDGD', 'tblq6rzmzxPY19fKV')

Number_of_facts = 5

for i in trending_topic_finder(Number_of_facts):
    crew=Crew(
        agents=[fact_finder_agent],
        tasks=[fact_finding_task],
        process=Process.sequential,
    )
    result=crew.kickoff(inputs={'topic':i})
    table.create(
        {
            'Topic':i,
            'Fact':result,
        }
    )
    time.sleep(1)
