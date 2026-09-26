from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()
#set page configuration
st.set_page_config(
    page_title="Chatbot",
    page_icon="🗣️",
    layout="centered"
)

st.title("Osaz Chatbot")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] #prevent unnecessary re initialization

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm initiatlization
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.0
)

user_prompt = st.chat_input("Ask Chatbot...")

#user sends message
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
