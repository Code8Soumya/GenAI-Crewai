import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

class TavilySearchTool():
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        tavily_tool = TavilySearchResults(
            max_results = 5,
            search_depth = "advanced",
            include_answer = True,
            include_raw_content = False,
            include_images = False,
        )
        results = tavily_tool.invoke(query)
        return results

