import os
from mem0 import Memory
from dotenv import load_dotenv
import json

load_dotenv()
from openai import OpenAI

client = OpenAI()

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")



config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config" : {"api_key": OPEN_AI_API_KEY , "model": "text-embedding-3-small"}
    },
    "llm":{
        "provider": "openai",
        "config" : {"api_key": OPEN_AI_API_KEY , "model": "gpt-4.1"}
    },
    "vector_store":{        
        "provider": "qdrant",
        "config" : { 
            "host": "localhost",
             "port": 6333,
        }    
    }
}

mem_client = Memory.from_config(config)

while True:
    user_query = input(">>>")
    search_memory = mem_client.search(query=user_query,user_id="kiran")
    
    memories = [
        f"ID: {mem.get('id')}\b Memory: {mem.get("memory")}" 
        for mem in search_memory.get("results")
    ]
    print("Available memories:",memories)

    SYSTEM_PROMPT = f"""
    Here is the context from memory: {json.dumps(memories)}.
    """


    response  = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": user_query
            }
        ],
        temperature=0.7,
        max_tokens=100
    )
    ai_response = response.choices[0].message.content


    print(f"���: {ai_response}")

    mem_client.add(
        user_id="kiran",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory updated successfully!")
