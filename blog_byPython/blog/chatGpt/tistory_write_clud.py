from time import sleep
import requests
import json
import openai

openai.api_key  = ''
messages = []
content = "한국어 할줄알아?"
messages.append({"role":"user", "content":content})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
messages.append({"role":"assistant", "content": chat_response})