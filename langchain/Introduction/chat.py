from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-4.1-mini")

ask = input("ask me a question: ")

response = llm.invoke(ask)

print(response.content)