import requests

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response =  requests.get(url)
    if response.status_code == 200:
        weather_data = response.text 
        return weather_data
    return "something went wrong"

print(get_weather("ponnur"))

         
        