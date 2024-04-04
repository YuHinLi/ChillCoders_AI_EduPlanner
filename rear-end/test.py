import requests

api_key = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
print(response.json())
