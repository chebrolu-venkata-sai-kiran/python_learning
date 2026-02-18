from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser ,JsonOutputParser
import streamlit as st

# Initialize the OpenAI Chat model

llm = ChatOpenAI(model_name="gpt-4.1-mini")

# Define the prompt template

product_prompt = PromptTemplate(
    input_variables=["product_name", "product_features"],
    template="""
    you are an expert in product management and marketing.
    create a catcy subject line for the following product: {product_name}
    highlight the following features: {product_features}
    respond with a subject line that is concise, engaging, and provides value to the recipient.
    """
)

email_prompt = PromptTemplate(
    input_variables=["subject_line", "product_name", "target_audience" ],
    template="""
    write a marketing email for the following product: {product_name}
    use the following subject line: {subject_line}
    Tailor the message to the following target audience: {target_audience}

    Format the output as a json object: with 3 keys: "subject_line", "audience", and "email_body"
    and fill with the appropriate values.

    """
)

first_chain = product_prompt | llm | StrOutputParser()

second_chain = email_prompt | llm | JsonOutputParser()

main_chain = first_chain |  (lambda subject_line: {"subject_line": subject_line, "product_name": product_name, "target_audience": target_audience }) | second_chain

st.title("Product Management & Marketing Automation")

product_name = st.text_input("Enter the product name")

product_features = st.text_input("Enter the features of the product (comma sperated)")

target_audience = st.text_input ("Enter the target audience")

if product_name and product_features and target_audience :
    result = main_chain.invoke({"product_name": product_name ,"product_features":product_features , "target_audience" : target_audience  })
    st.write(result)