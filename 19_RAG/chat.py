from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"    
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings,
)

# take user input for the query

user_input = input("Enter your query: ")

#similarity search

search_results = vector_db.similarity_search(query=user_input, k=3)



context = "\n\n\n".join( [
    f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}  File Location: {result.metadata['source']}" for result in search_results ])

SYSTEM_PROMPT = f"""
you are a helpful AI assistant. You will be given a list of documents related to the user's query.
 Your task is to summarize the most relevant document(s) in a concise and informative manner.
 retrived from a pdf file along with the page number for each document.

 you should only ans the user based in the following context and navigate the user to open the right page number to know more

 context:{context}
 """

response = openai_client.chat.completions.create(
    model="gpt-4.1-mini",
    messages= [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input},
    ]
)

print(f"🤖: {response.choices[0].message.content}")