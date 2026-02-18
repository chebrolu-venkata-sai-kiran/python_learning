from dotenv import load_dotenv
import numpy as np
load_dotenv()

from langchain_openai import OpenAIEmbeddings
llm = OpenAIEmbeddings()

a1 = input("Enter the first text: ")
a2 = input("Enter the second text: ")

r1 = llm.embed_query(a1)
r2 = llm.embed_query(a2)

similarity = np.dot(r1, r2)
print(f"Similarity: {similarity}")

