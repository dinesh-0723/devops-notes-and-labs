#pip3 install openai
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
client = AzureOpenAI (azure_endpoint="https://zix.openai.azure.com/",
api_key = os.getenv("AZURE_OPENAI_KEY"),
api_version = "2025-04-01-preview")
print("Welcome To ChatBoat!")
while True:
    msg = input("You: ")
    if msg == 'quit':
        break
    response = client.chat.completions.create(
        #model = 'gpt-5-mini',
        model = 'gpt-5.1-chat',
        messages = [{"role":"user", "content": msg}],
        max_completion_tokens=500
    )
    print(f"Chatbot: {response.choices[0].message.content}\n")