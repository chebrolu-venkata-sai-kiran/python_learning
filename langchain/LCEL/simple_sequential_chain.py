from langchain_core.prompts import PromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
 
from langchain_openai import ChatOpenAI
api_key=os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-4.1-mini",api_key=api_key)

title_template = PromptTemplate(
    input_variables=["topic"],
    template="""
    you are an experienced speech writer you need to create a title for the provided {topic}.
    Answer exactly with only one title.
    """
)


speech_template = PromptTemplate(
    input_variables=["title"],
    template="""
    you are an experienced speech writer you need to create a powerfull speechof 350 words for the provided {title}.
    
    """
)

first_chain = title_template | llm | StrOutputParser() | (lambda title : (st.write("Title: ", title),title)[1])
second_chain = speech_template | llm 
final_chain = first_chain | second_chain  

st.title("Speech Expert")

topic = st.text_input("Enter the topic name", )



if topic:
    result = final_chain.invoke({"topic": topic})
    st.write(result.content)



