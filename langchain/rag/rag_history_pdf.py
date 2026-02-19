from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings ,ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import  RunnableWithMessageHistory
import streamlit as st
from langchain_classic.chains import create_retrieval_chain ,create_history_aware_retriever 
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

#llms
embedings = OpenAIEmbeddings()
llm = ChatOpenAI(model_name="gpt-4.1-mini")

# Load the product data
document_loader = PyPDFLoader("gym.pdf").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
chunks = text_splitter.split_documents(documents=document_loader)
vector_store = Chroma.from_documents(chunks, embedings)
retriver = vector_store.as_retriever()


prompt_template = ChatPromptTemplate.from_messages(

[
    ("system", "You are an AI assistant for answering questions related to the product data."
    "use the rpovided context to respond if answer isn't cleat acknowledge that you don't know the answer."
    "limit your response to 3 sentences.{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}"),

]

)

# Create the chain
history_aware_retriver = create_history_aware_retriever(llm,retriver,prompt_template)
qa_chain = create_stuff_documents_chain(llm,prompt_template)
rag_chain = create_retrieval_chain(history_aware_retriver,qa_chain)

history_for_chain = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id:history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

st.title("Welcome to the Product Data Assistant!")



question = st.text_input("Ask a question: ")
 
if question:
    response = chain_with_history.invoke({"input": question},{"configurable":{"session_id": "1234567890"}})
    st.write(response['answer'])