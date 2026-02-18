from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
 
from langchain_openai import ChatOpenAI
api_key=os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-4.1-mini",api_key=api_key)

prompt_template = ChatPromptTemplate.from_messages(
  
    [
        ("system","you are an agile coach answer any questions realted to the agile process"),
        ("human","{input}")
    ]
)

st.title("Agile Expert")

input = st.text_input("Enter the agile questions", )

chain = prompt_template | llm

if input :
    result = chain.invoke( {"input":input})
    st.write(result.content)



