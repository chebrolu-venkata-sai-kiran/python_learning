from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
import streamlit as st




import base64

# Function to encode an image into base64 format for the chatbot to understand.

def encode_image(image_file):
    
        return base64.b64encode(image_file.read()).decode()



# Initialize the ChatOpenAI model with the specified model.
llm = ChatOpenAI(model="gpt-4.1-mini")
# image = encode_image("airport_terminal_journey.jpeg")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64 ,"" {image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm

# Example usage:

upload_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

question = st.text_input("enter your question ?")

if question and upload_file :
    image = encode_image(upload_file)
    response = chain.invoke({"input": question,"image": image})
    st.write(response.content)