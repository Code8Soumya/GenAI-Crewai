from crewai import Task
from agents import fact_finder_agent
from tools import TavilySearchTool

fact_finding_task = Task(
    description=(
        'Quickly find the most interesting and engaging fact about {topic}. '
        'Present only the fact in a concise and engaging manner, ensuring it is sourced from reliable information. '
        'Avoid any opinions or speculation. Focus on speed and accuracy.'
    ),
    expected_output=(
        'Output only the most interesting facts about {topic}. '
        'Present them concisely and in an engaging way for a general audience. '
        'Example: Did you know the world\'s oldest piece of chewing gum is 9,000 years old? It wasn\'t Juicy Fruit, but birch bark tar used by a Stone Age person in Finland. '
        'Example: The population of the earth is about 8 billion people, roughly the same number of stars in our Milky Way galaxy. '
        'Example: What do the Eiffel Tower and the Statue of Liberty have in common? They both shrink in the winter!'
    ),
    agent=fact_finder_agent,
    tools=[TavilySearchTool.search_internet],
)