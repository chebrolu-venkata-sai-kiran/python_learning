from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings ,ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

#llms
embedings = OpenAIEmbeddings()
llm = ChatOpenAI(model_name="gpt-4.1-mini")

# Load the product data
document_loader = TextLoader("product.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
chunks = text_splitter.split_documents(documents=document_loader)
vector_store = Chroma.from_documents(chunks, embedings)
retriver = vector_store.as_retriever()


prompt_template = ChatPromptTemplate.from_messages(

[
    ("system", "You are an AI assistant for answering questions related to the product data."
    "use the rpovided context to respond if answer isn't cleat acknowledge that you don't know the answer."
    "limit your response to 3 sentences.{context}"),
    ("human","{input}"),

]

)

# Create the chain

qa_chain = create_stuff_documents_chain(llm,prompt_template)
rag_chain = create_retrieval_chain(retriver,qa_chain)

print("Welcome to the Product Data Assistant! Type 'exit' to quit.")


while True:
    question = input("Ask a question: ")
    if question.lower() == "exit":
        break
    response = rag_chain.invoke({"input": question})
    print(response['answer'])