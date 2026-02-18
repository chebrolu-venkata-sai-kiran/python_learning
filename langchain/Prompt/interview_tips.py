import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4.1-mini",
                 api_key=OPENAI_API_KEY,
                  )

prompt_template = PromptTemplate(
    input_variables=["company", "position", "strengths", "weaknesses"],
    template="""You are a career coach. Provide tailored interview preparation tips for a candidate applying to {company} for the position of {position}.
    Consider the candidate's strengths: {strengths} and weaknesses: {weaknesses}.
    Offer advice on how to leverage strengths and address weaknesses during the interview.
    """)

st.title("Interview Preparation Helper")

company = st.text_input("Company: ")
position = st.text_input("Position")
strengths = st.text_area("Strengths", height=100)
weaknesses = st.text_area("Weaknesses", height=100)

if company and position and strengths and weaknesses:
    response = llm.invoke(prompt_template.format(company=company, position=position, strengths=strengths, weaknesses=weaknesses))
    st.write(response.content)