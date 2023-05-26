# Custom AI Chatbot Trainer

This project is a custom AI chatbot trainer that utilizes the Llama Index library to create a chatbot capable of generating responses to user queries based on a pre-trained GPT (Generative Pre-trained Transformer) language model. The chatbot is trained on a set of documents in a directory and uses the Llama Index for efficient querying.

## Dependencies

The project has the following dependencies:

- Llama Index (version 0.5.4)
- LangChain (version 0.0.127)
- OpenAI Python SDK
- Gradio (for creating the chatbot interface)
- Python 3.8 or higher

## Setup

To set up the project, follow these steps:

1. Clone the repository:
2. Install the required dependencies:
   ```
   git clone https://github.com/CKawara/Custom-AI-Chatbot-Trainer.git
   ```

3. Set up your OpenAI API key:
  - Obtain an API key from OpenAI (https://openai.com).
  - Create a file named .env in the project directory.
  - Add the following line to the .env file, replacing <YOUR_API_KEY> with your actual OpenAI API key:  
    ```
      export OPENAI_API_KEY=your-api-key
    ```
4. Prepare your training documents:
  - Place your training documents in the docs directory and specify the path to that directory in the directory_path variable in the script.
5. Run the application:
  ```
  python3 app.py

  ```
