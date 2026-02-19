from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()



import base64

# Function to encode an image into base64 format for the chatbot to understand.

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()



# Initialize the ChatOpenAI model with the specified model.
llm = ChatOpenAI(model="gpt-4o")
image = encode_image("airport_terminal_journey.jpeg")
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
                        "url": f"data:image/jpeg;base64,{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm

# Example usage:

response = chain.invoke({"input": "explain the image? "})
print(response.content)