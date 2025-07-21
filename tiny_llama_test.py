from llama_cpp import Llama

llm = Llama(
    model_path=r"C:\Users\super\OneDrive\Documents\Desktop\ToppoBot\models",  # replace with actual path
    n_ctx=2048,
    chat_format="chatml"
)

# Sample chat prompt
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

output = llm.create_chat_completion(messages)
print(output['choices'][0]['message']['content'])
