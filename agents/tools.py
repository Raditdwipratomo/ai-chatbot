from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools(enable: bool):
    return [TavilySearchResults(max=2)] if enable else []

