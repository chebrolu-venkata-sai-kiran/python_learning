from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "git.pdf"

#Load this file in the python program
loader  = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

# print the first page content
# print(docs[0].page_content)

# Split the documents into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )

chunks = text_splitter.split_documents(documents=docs)

# Embedding model

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"    
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url = "http://localhost:6333",
    collection_name="learning_rag"     
)

print("Vector Store is ready...")