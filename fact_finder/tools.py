import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from pytrends.request import TrendReq


os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

class TavilySearchTool():
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        tavily_tool = TavilySearchResults(
            max_results = 3,
            search_depth = "advanced",
            include_answer = True,
            include_raw_content = False,
            include_images = False,
        )
        results = tavily_tool.invoke(query)
        return results
    
def trending_topic_finder(number_of_topics:int = 5) -> list:
    pytrend = TrendReq()
    df = pytrend.trending_searches(pn='india')
    return df[0].tolist()[:number_of_topics]
