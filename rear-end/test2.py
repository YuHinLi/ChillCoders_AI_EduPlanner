import requests

api_key = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 初始化对话历史
conversation_history = []


# 函数：向GPT发送消息，并更新对话历史
def send_message_to_gpt(content):
    # 将用户的消息添加到对话历史
    conversation_history.append({"role": "user", "content": content})

    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
        "temperature": 0.7
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    reply = response.json()

    # 将模型的回复添加到对话历史
    if reply.get("choices"):
        model_reply_content = reply["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": model_reply_content})
        print("GPT:", model_reply_content)
    else:
        print("Error:", reply)


# 发送第一条消息
send_message_to_gpt("Say this is a test!")

# 继续发送更多消息
send_message_to_gpt("What do you know about Python?")
