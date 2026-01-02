import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Chatbot", layout="centered")

st.title("AI Agent Chatbot")
st.markdown("Chat with multiple model with web search.")

with st.sidebar:
    st.header("Agent configuration")
    model_provider = st.selectbox("Model Provider", ["Groq", "Deepseek"])

    model_name = st.selectbox("Model Name", ["llama-3.1-8b-instant", "deepseek/deepseek-r1-0528:free"])

    system_prompt = st.text_area(
        "System Prompt",
        value="Act as an Personal Smart AI assitant",
        height=100
    )

    allow_search = st.checkbox("Enable web search tool", value=False)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

# Display chat history

for role, msg in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("User"):
            st.markdown(msg)
    else:
        with st.chat_message("ai"):
            st.markdown(msg)

# Handle user input

user_query = st.chat_input("Type your query...")

if user_query:
    with st.chat_message("User"):
        st.markdown(user_query)
    st.session_state.chat_history.append(("User", user_query))

    # Send request to backend
    with st.chat_message("ai"):
        with st.spinner("Thinking...."):
            try:
                payload = {
                    "model_name": model_name,
                    "model_provider": model_provider,
                    "system_prompt": system_prompt,
                    "messages": [user_query],
                    "allow_search": allow_search
                }

                res = requests.post("http://127.0.0.1:8000/chat", json=payload)
                response = res.json()

                st.markdown(response)
                st.session_state.chat_history.append(("ai", response))
            except Exception as e:
                st.error(f"Error: {e}")






