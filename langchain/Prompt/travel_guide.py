from langchain_core.prompts import PromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
 
from langchain_openai import ChatOpenAI
api_key=os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-4.1-mini",api_key=api_key)

prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template="""
    you are an expert in the traveling suggestion.
    now i want you to give me the travel suggestion for {city} 
    1.Must visit places.
    2.must try cusines.
    3.which month you are planing to visit {month}.
    4.give me few phrases that will use it in the {language}.
    5.tell me the budget {budget}.

    have a great holiday!
    """
)

st.title("Travel Expert")

city = st.text_input("Enter the city name", )
month = st.text_input("Enter the month ")
language = st.text_input("Enter the language " )
budget = st.selectbox("Enter the budget ",["low","medium","high"])


if city and month and language and budget:
    result = llm.invoke(prompt_template.format(city=city,month=month,language=language,budget=budget))
    st.write(result.content)



