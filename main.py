import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

def init():
    # Load OpenAI key from environment variables
    load_dotenv()

    #test that the key is set
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    #setup the page
    st.set_page_config(
        page_title="MyChatgpt", 
        page_icon=":material/chat:"
    )
    
def main():
    init()

    chat = ChatOpenAI(temperature=0)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # Header with image
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image("https://cdn-icons-png.freepik.com/512/3593/3593684.png", width=60)
    with col2:
        st.header("My Query Solver")

    # Sidebar with user input
    with st.sidebar:
        user_input = st.text_input("Enter your text here", key="user_input")
        
        #handle user input
        if user_input:
                st.session_state.messages.append(HumanMessage(content=user_input))
                with st.spinner("Thinking..."):
                    response = chat(st.session_state.messages)
                st.session_state.messages.append(
                    AIMessage(content=response.content))
                

    # Display chat history
    messages = st.session_state.get("messages", [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == "__main__":
    main()