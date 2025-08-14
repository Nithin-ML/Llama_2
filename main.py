from llama_model import llama_chat
from pytt_audio import speak

def main():
    while True:
        input_prompt = input("You: ")
        if input_prompt.lower() in ["exit", "quit"]:
            break
        response = llama_chat(input_prompt)
        print(f"Llama: {response}")
        speak(response)  # Vocalize the response

if __name__ == "__main__":
    main()