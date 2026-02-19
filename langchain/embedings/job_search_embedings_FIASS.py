from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma 
from langchain_community.vectorstores import FAISS


llm = OpenAIEmbeddings()

# question = input("Please provide a question: ")

document_loader = TextLoader("job.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
chunks = text_splitter.split_documents(documents=document_loader)
db = FAISS.from_documents(chunks, llm)
retriver = db.as_retriever()
 
text = input("Please provide a question: ")
# emebed_text = llm.embed_query(text)

# docs = db.similarity_search_by_vector(emebed_text)

docs = retriver.invoke(text)

for doc in docs:
    print(doc.page_content)