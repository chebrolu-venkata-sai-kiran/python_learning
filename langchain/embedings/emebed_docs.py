from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
          
)

# question = input("Please provide a question: ")

response = embeddings.embed_documents([

    "my name is kiran",
    "my age is 30",
    "my hobby is playing basketball"
])

# print(f"The embeddings for the question '{question}' are: {response}")
print(len(response))
print(response[0])