from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="🗣️",
    layout="centered"
)

st.title("GenAI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

