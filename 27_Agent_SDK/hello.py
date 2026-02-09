from dotenv import load_dotenv
load_dotenv()
from agents import Agent,Runner

hello_agent = Agent(
    name= "Hello World Agent",
    instructions="you are an agent which greets the user with smile and ans them using emoji in a funnyway",
  )

result = Runner.run_sync(hello_agent, input="Hello, Agent! my name is John")

print(result.final_output)

