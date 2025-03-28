# main.py
"""
Streamlit-based UI for Amina's Recruitment Chatbot.
This chatbot interacts with users to provide details about Amina's qualifications, experience, and skills in data science.
"""

import streamlit as st
from chatbot import generate_response

def initialize_session():
    """Initialize session state for chat history."""
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

def display_chat_history():
    """Display previous messages in chat history."""
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

def main():
    """Main function to run Streamlit chatbot UI."""
    st.title("Amina's Recruitment Chatbot")
    st.chat_message("assistant").write("Hello! I'm your recruitment chatbot. Ask me questions about Amina's qualifications, experience, skills, or data science!")
    initialize_session()
    display_chat_history()

    user_input = st.chat_input("Ask about Amina's qualifications, experience, skills, or data science:")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        response = generate_response(user_input)
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state["messages"].append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
