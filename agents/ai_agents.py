from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from agents.llm_provider import get_llm
from agents.tools import get_tools

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    llm = get_llm(provider, llm_id)
    tools = get_tools(allow_search)

    agent = create_react_agent(model=llm, tools=tools)

    # To build conversation history
    state = {
        "message": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query[-1])
        ]
    }

    response = agent.invoke(state)
    messages = response.get("messages", [])
    ai_message = [msg.content for msg in messages if isinstance(msg.AIMessage)]
    return ai_message[-1] if ai_message else "No Response"

