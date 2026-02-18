import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.globals import set_debug
import os

set_debug(True)  # Enable debugging mode for LangChain

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4.1-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)


st.title("this is the sample streamlit")

ask = st.text_input("Ask a question")

if ask:
    result = llm.invoke(ask)
    st.write(result.content)