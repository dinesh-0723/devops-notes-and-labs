from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint="https://devopsazopenai.openai.azure.com/",
    api_version="2024-02-15-preview"
)

deployment="gpt-4o-mini"

def ask_ai(question):

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role":"system","content":"You are a DevOps assistant."},
            {"role":"user","content":question}
        ]
    )

    return response.choices[0].message.content