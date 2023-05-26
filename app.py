from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext
from langchain import OpenAI
import gradio as gr
import os
import dotenv

# Load the API key from the .env file
dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def construct_index(directory_path):
    num_outputs = 512

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    # Load documents from the directory
    docs = SimpleDirectoryReader(directory_path).load_data()

    # Create and save the index
    index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)
    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    # Load the index from disk
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    # Query the index for a response
    response = index.query(input_text, response_mode="compact")
    
    return response.response

# Create the Gradio interface
iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot for all your Machine learning questions")

# Specify the directory path
directory_path = "docs"

# Construct the index from the documents directory
index = construct_index(directory_path)

# Launch the Gradio interface
iface.launch(share=True)
