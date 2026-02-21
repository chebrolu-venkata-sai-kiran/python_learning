import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug
 
set_debug(True)  # Enable debugging mode for LangChain


st.title("this is the sample streamlit")

with st.sidebar:
    st.title("provide your OpenAI API Key")
    api_key = st.text_input("API Key",type="password")
if not api_key:
    st.warning("Please provide an OpenAI API Key")
    st.stop()

llm = ChatOpenAI(
    model_name="gpt-4.1-mini",
    openai_api_key= api_key
)

ask = st.text_input("Ask a question")

if ask:
    result = llm.invoke(ask)
    st.write(result.content)