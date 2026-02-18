from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser



api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4.1-mini", api_key=api_key)

outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    you are an expert in writing blog posts.create a blog post about {topic} using the following guidelines:
    1. write a concise and engaging title.
    2. write a clear and concise introduction.
    3. write a detailed and thought-provoking body.
    """
)

introduction_prompt = PromptTemplate(
    input_variables=["outline"],
    template="""
    you are an expert in writing blog posts.create a blog post about {outline} using the following guidelines:
    write an engaging introduction based on the outline provided.
    the introduction should be hook the reader and set the tone for the rest of the post.
    """
)

first_chain = outline_prompt | llm | StrOutputParser()
second_chain = introduction_prompt | llm 

final_chain = first_chain | second_chain

st.title("Blog Writer")

topic = st.text_input("Enter a topic for your blog post")

if topic:
    result  =  final_chain.invoke({"topic": topic})
    st.write(result.content)



