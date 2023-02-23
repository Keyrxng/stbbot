from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os

os.environ['OPENAI_API_KEY']

def ask_ai(user_msg):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        response = index.query(user_msg, response_mode="compact")
        return response.response