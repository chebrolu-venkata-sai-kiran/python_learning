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
        ("system", "You are a helpful assistant that can verify identification documents."),
        (
            "human",
            [
                {"type": "text", "text": "verify the identification details of the person in the image."},
                {"type": "text", "text": "Name : {user_name}"},
                {"type": "text", "text": "DOB :  {user_dob}"},
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

st.title("Verification Assistant")

st.write("Welcome to the Verification Assistant!")

st.write("Please upload your document for verification.")

# Example usage:

upload_file = st.file_uploader("Upload document", type=["jpg", "jpeg", "png"])

user_name = st.text_input("Enter your name")

user_dob = st.date_input("Enter your date of birth")


if user_dob and user_name and upload_file is not None :
    image = encode_image(upload_file)
    response = chain.invoke({"user_name": user_name,"user_dob": user_dob ,"image": image})
    st.write(response.content)