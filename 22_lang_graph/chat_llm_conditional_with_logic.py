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
    
    llm_response = state.get("llm_response", "")
    
    # Validation criteria for a good response
    is_good = True
    
    # Check if response exists and is not empty
    if not llm_response or llm_response.strip() == "":
        is_good = False
        print("Response is empty or None")
    
    # Check response length (too short might indicate poor quality)
    elif len(llm_response.strip()) < 10:
        is_good = False
        print("Response is too short")
    
    # Check for common error patterns or unhelpful responses
    elif any(phrase in llm_response.lower() for phrase in [
        "i cannot", "i can't", "i'm sorry", "i don't know",
        "error", "unable to", "cannot provide", "not possible"
    ]):
        is_good = False
        print("Response contains error patterns or unhelpful phrases")
    
    # Check if response is relevant to the query (basic keyword matching)
    elif state.get("user_query"):
        query_words = state["user_query"].lower().split()
        # For math queries, check if response contains numbers or math terms
        if any(word in state["user_query"].lower() for word in ["1+1", "+", "math", "calculate"]):
            if not any(char.isdigit() for char in llm_response):
                is_good = False
                print("Math query response doesn't contain numbers")
    
    # Update state with evaluation result
    state["is_good"] = is_good
    
    print(f"Response evaluation: {'GOOD' if is_good else 'BAD'}")
    print(f"Response content: {llm_response[:100]}...")
    
    # Route based on evaluation
    if is_good:
        return "endnode"  # Good response, proceed to end
    else:
        return "chatbot_updated"  # Bad response, try updated chatbot


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

updated_state = graph.invoke(State({"user_query" : "what is 0 divided by infinete ?"}))

print(updated_state)




