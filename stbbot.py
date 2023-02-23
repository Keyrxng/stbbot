from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os

os.environ['OPENAI_API_KEY']

# def construct_index(directory_path):
#     # set maximum input size
#     max_input_size = 4096
#     # set number of output tokens
#     num_outputs = 300
#     # set maximum chunk overlap
#     max_chunk_overlap = 20
#     # set chunk size limit
#     chunk_size_limit = 600 

#     # define LLM
#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
#     prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
#     documents = SimpleDirectoryReader(directory_path).load_data()
    
#     index = GPTSimpleVectorIndex(
#         documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
#     )

#     index.save_to_disk('index.json')

#     return index

def ask_ai(user_msg):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        response = index.query(user_msg, response_mode="compact")
        return response.response