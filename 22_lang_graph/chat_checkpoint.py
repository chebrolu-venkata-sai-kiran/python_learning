from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph , START , END
from langchain.chat_models import init_chat_model  
from langgraph.checkpoint.mongodb import MongoDBSaver 





# initialize OpenAI LLM model for chatbot interaction

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider= "openai"
)


class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages")  )
    return {"messages": [response]}

 



graph_bulider = StateGraph(State)

graph_bulider.add_node("chatbot",chatbot)
 

graph_bulider.add_edge(START,"chatbot")
graph_bulider.add_edge("chatbot",END)
 

graph = graph_bulider.compile()


def compile_graph_with_checkpointer(checkpointer):
    return graph_bulider.compile( checkpointer=checkpointer)


# initialize MongoDB saver to save the graph and configurations

DB_URL = "mongodb://admin:admin@localhost:27017/"
with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:

    
     
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "sai"
        }
    }
    while True:
        print("================================== user input ==================================")
        for chunk in graph_with_checkpointer.stream(
            
            State({"messages" : [input("Enter your input: ")]}),
            config,
            stream_mode="values"
            ):
            chunk["messages"][-1].pretty_print()

    # print("\n\nupdated state",updated_state)




