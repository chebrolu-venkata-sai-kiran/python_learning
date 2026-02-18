from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
          
)

question = input("Please provide a question: ")

response = embeddings.embed_query(question)

print(f"The embeddings for the question '{question}' are: {response}")