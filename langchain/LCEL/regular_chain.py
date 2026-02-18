from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser
 
from langchain_openai import ChatOpenAI
 

llm = ChatOpenAI(model="gpt-4.1-mini")

title_template = PromptTemplate(
    input_variables=["topic"],
    template="""
    you are an experienced speech writer you need to create a title for the provided {topic}.
    Answer exactly with only one title.
    """
)


speech_template = PromptTemplate(
    input_variables=["title" , "emotion"],
    template="""
    you are an experienced speech writer you need to create a powerfull {emotion} speechof 350 words for the provided {title}.
    Format for the output with 3 keys : 'title' , 'emotion' and 'speech' and fill it with the respective details.
    """
)

first_chain = title_template | llm | StrOutputParser() | (lambda title : (st.write("Title: ", title),title)[1])
second_chain = speech_template | llm  | JsonOutputParser()
final_chain = first_chain |(lambda title : {"title":title , "emotion":emotion}) | second_chain  

st.title("Speech Expert")

topic = st.text_input("Enter the topic name :" )
emotion = st.text_input("Enter the emotion :" )




if topic and emotion:
    result = final_chain.invoke({"topic": topic})
    st.write(result)



