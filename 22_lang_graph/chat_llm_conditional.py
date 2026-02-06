from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict
from langgraph.graph import StateGraph , START , END
from typing import   Optional,Literal
from openai import OpenAI
client = OpenAI()



class State(TypedDict):
    user_query: str
    llm_response: Optional[str]
    is_good: Optional[bool] 


def chatbot(state: State):
    print("\n\ninside chatbot function",state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            
            {"role": "user", "content": state.get("user_query")}
        ]
    )
    state["llm_response"] = response.choices[0].message.content
    return state

def evaluate_response(state: State)-> Literal["chatbot_updated", "endnode"]:
    print("\n\ninside evaluate_response function",state)

    if False:
        return "endnode"
    
    return "chatbot_updated"


def chatbot_updated(state: State):
    print("\n\ninside chatbot_updated function",state)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            
            {"role": "user", "content": state.get("user_query")}
        ]
    )
    state["llm_response"] = response.choices[0].message.content
    return state

def endnode(state: State):
    print("\n\ninside endnode function",state)
    return state



graph_bulider = StateGraph(State)

graph_bulider.add_node("chatbot",chatbot)
graph_bulider.add_node("chatbot_updated",chatbot_updated)
graph_bulider.add_node("endnode",endnode)

graph_bulider.add_edge(START,"chatbot")
graph_bulider.add_conditional_edges("chatbot", evaluate_response)
graph_bulider.add_edge("chatbot_updated", "endnode")
graph_bulider.add_edge("endnode", END)

graph = graph_bulider.compile()

updated_state = graph.invoke(State({"user_query" : "what is 1+1 ?"}))

print(updated_state)




