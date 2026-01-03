from google import genai

client = genai.Client(
    api_key='AIzaSyAeRJB3aVS0Ntg-cxBOQ-uYBjw8hGS7wOc'
)

response = client.models.generate_content(
    model = 'gemini-2.5-flash',contents = 'What is the capital of France?')

print(response.text)