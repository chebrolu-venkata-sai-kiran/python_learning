
import requests

try:
    response = requests.get("https://api.openai.com/v1/models", timeout=10)
    print(f"Connection test status: {response.status_code}")
except Exception as e:
    print(f"Connection test failed: {e}")
