# import torch

# print(torch.cuda.is_available())   # True if CUDA GPU is detected
# print(torch.cuda.device_count())   # Number of GPUs detected
# print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")


# import llama_cpp
# print("CUDA Enabled:", llama_cpp.llama_cuda_available())

from llama_cpp import Llama

llm = Llama(model_path="Llama_2_7b\llama-2-7b-chat.Q8_0.gguf", n_gpu_layers=1)
print(llm.__dict__.get("_model", None))  # sometimes shows backend info

