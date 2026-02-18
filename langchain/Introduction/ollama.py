import os
from langchain_ollama import ChatOllama

# to use this we need to have the ollama installed in our local machine and need to pull the images or models which
# we are planning to use 

llm = ChatOllama(model="mistral")

question = input("What is the question? ")
response = llm.invoke(question)
print(response.content)