from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI 

client = OpenAI()

response  = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role":"user",
            "content" : [
               { "type":"text",  "text":"give me a caption for this image in 50 words?"},
               {"type":"image_url", "image_url":{"url": "https://images.pexels.com/photos/7114/laptop-mobile.jpg"}}

            ]
        }

    ]
)

print("response",response.choices[0].message.content)