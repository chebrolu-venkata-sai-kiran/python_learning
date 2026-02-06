from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph , START , END
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider= "openai"
)


class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages")  )
    return {"messages": [response]}

def samplenode(state: State):
    print("\n\ninside samplenode function",state)    
    return {"messages": ["sample node"]}



graph_bulider = StateGraph(State)

graph_bulider.add_node("chatbot",chatbot)
graph_bulider.add_node("samplenode",samplenode)


graph_bulider.add_edge(START,"chatbot")
graph_bulider.add_edge("chatbot","samplenode")
graph_bulider.add_edge("samplenode",END)


graph = graph_bulider.compile()

updated_state = graph.invoke(State({"messages" : ["Hello, my name is kiran"]}))

print("\n\nupdated state",updated_state)




