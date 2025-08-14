# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# model_id = "Llama_2_7b/llama"
# tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir="./llama_local")
# model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir="./llama_local")

# # Example prompt
# prompt = "Hello, how can I help you today?"

# # Tokenize input
# inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# # Generate response
# with torch.no_grad():
#     outputs = model.generate(**inputs, max_new_tokens=100)
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# print(response)

from llama_cpp import Llama
from pytt_audio import speak

# Point to your local GGUF file
llm = Llama(
    model_path="Llama_2_7b\llama-2-7b-chat.Q8_0.gguf",
    n_ctx=8192,            # context window
    n_gpu_layers=32,       # -1 = offload all layers to GPU (if available)
    n_threads=8,           # CPU threads
    chat_format="llama-3",
    verbose=False # important for role-based chat with Llama 3 Instruct
)
def llama_chat(input_prompt):
    messages = [
        {"role": "system", "content": "You are a helpful, concise assistant."},
        {"role": "user", "content": input_prompt}
    ]

    resp = llm.create_chat_completion(
        messages=messages,
        max_tokens=500,
        temperature=0.7,
        top_p=0.95,
    )
   
    return resp["choices"][0]["message"]["content"]
# while True:
#     input_prompt = input("You: ")
#     messages = [
#         {"role": "system", "content": "You are a helpful, concise assistant."},
#         {"role": "user", "content": input_prompt}
#     ]

#     resp = llm.create_chat_completion(
#         messages=messages,
#         max_tokens=500,
#         temperature=0.7,
#         top_p=0.95,
#     )
   
#     assistant_text = resp["choices"][0]["message"]["content"]
#     print(f"Llama : {assistant_text}")
    # speak(assistant_text)  # Use the speak function to vocalize the response
