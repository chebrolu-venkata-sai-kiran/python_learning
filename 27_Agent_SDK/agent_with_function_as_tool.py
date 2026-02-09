from dotenv import load_dotenv
load_dotenv()
from agents import Agent,Runner,WebSearchTool,function_tool

import requests
@function_tool
def get_weather(city: str):
    """
    Docstring for get_weather
    Fetch the weather for the given city name
    :param city: Description
    :type city: str
    """ 
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response =  requests.get(url)
    if response.status_code == 200:
        weather_data = response.text 
        return weather_data
    return "something went wrong"


hello_agent = Agent(
    name= "Hello World Agent",
    instructions="you are an agent which greets the user with smile and ans them using emoji in a funnyway",
    tools=[
        #WebSearchTool()
        get_weather
    ]
  )

result = Runner.run_sync(hello_agent, input="Hello, Agent! my name is John,what is the weather todayin pune?")

print(result.final_output)
print(result.raw_responses)

