from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

from langchain_openai import ChatOpenAI
api_key=os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-4.1-mini",api_key=api_key)

prompt_template = PromptTemplate(
    input_variables=["country","no_of_paras","language"],
    template="""
    you are an expert in traditional cuisines.you provide the information about a specific dish from a specific country.
    Avoid giving information about the ficitional places if something is non existing answer to it as : I Don't Know
    Answer the question : what is the traditional cuisine of the {country}?
    Answer in the {no_of_paras} in {language}.
    """
)

st.title("Traditional Cuisine Expert")

country = st.text_input("Enter the country name", key="first_input_key")
no_of_paras = st.number_input("Enter the number of paragraphs",min_value=1,max_value=10)
language = st.text_input("Enter the language ", key="second_input_key")

if country:
    result = llm.invoke(prompt_template.format(country=country,no_of_paras=no_of_paras,language=language))
    st.write(result.content)



