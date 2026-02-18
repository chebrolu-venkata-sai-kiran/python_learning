from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.runnables.history import  RunnableWithMessageHistory
# import streamlit as st

llm = ChatOpenAI(model="gpt-4.1-mini")

prompt_template = ChatPromptTemplate.from_messages(

[
("system", "You are an AI assistant. You will be given a task. You must generate a detailed and long answer related"
"to the Agile "),
MessagesPlaceholder(variable_name="chat_history"),
("human","{input}")


]

)

chain = prompt_template | llm


history_for_chain = ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id:history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

print("Agile Guide")

while True:

    input_text = input("Enter Agile topic")

    if input_text:
        result = chain_with_history.invoke({"input": input_text},{"configurable":{"session_id": "1234567890"}})
        print(result.content)

# st.write("history_for_chain" )

# st.write(history_for_chain)



