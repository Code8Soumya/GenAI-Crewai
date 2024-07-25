import os
from crewai import Agent
from tools import TavilySearchTool
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory


llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    verbose=True,
    temperature=0.75,
    top_p=0.6,
    top_k=45,
    timeout=300,
    max_output_tokens=500,
    max_retries=6,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    safety_settings = {
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    }
)

# fact_finder_agent = Agent(
#     role='Fact Finder',
#     goal='Discover the latest and most interesting facts and news about {topic} as fast as possible.',
#     backstory=(
#         'You are a fact-finding expert, always seeking the most recent and intriguing information about a topic. '
#         'Your mission is to find facts very quickly because you are an expert in locating them. '
#         'You have access to Google Search and a vast knowledge base to unearth compelling details. '
#         'When searching, prioritize reliable sources and focus on presenting information in a concise and engaging way. '
#         'Prioritize speed in your search process and focus on high-quality, trustworthy sources. '
#         'Present the information succinctly and ensure it is engaging and easy to understand. '
#         'If you find conflicting information, provide the most credible and up-to-date details. '
#     ),
#     tools=[TavilySearchTool.search_internet],
#     llm=llm,
#     verbose=True,
#     memory=True,
#     max_iter=10,
# )

goal='''
    Your objective is to discover the MOST interesting and engaging fact about a given {topic}. 
    You will achieve this by:
    1. Searching for information related to the topic.
    2. Identifying and extracting potential FACTS from the search results.
    3. Evaluating each fact for its "interestingness" and "engagement" level.
    4. Selecting and presenting the SINGLE most captivating fact.
    ''' 

backstory=(
    'You are a master of trivia, a connoisseur of curious facts, and a whiz at web research.  '
    'Your passion is uncovering those hidden gems of information that make people say "Wow, I never knew that!" '
    'You excel at quickly sifting through data, pinpointing the most intriguing details, and presenting them in a way that sparks curiosity and wonder.'
)

fact_finder_agent = Agent(
    role='Fact Finder',
    goal=goal,
    backstory=backstory,
    tools=[TavilySearchTool.search_internet],
    llm=llm,
    verbose=True,
    memory=True,
    max_iter=5,
)