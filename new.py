import threading
import itertools
import time
from gpt4all import GPT4All

# Loading animation function
def loading_animation():
    for frame in itertools.cycle(["|", "/", "-", "\\"]):
        if not loading_flag:  # Stop if loading_flag is set to False
            break
        print(f"\rChatbot is thinking... {frame}", end="")
        time.sleep(0.1)

def mental_health_chat():
    model_path = "C:/Users/Siddharth/gpt4all/bin"
    
    try:
        model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf", model_path=model_path, allow_download=False)
        print("Mental Health Care Chatbot is ready! Type 'exit' to end the conversation.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Take care! Remember, seeking help is a sign of strength. Goodbye!")
                break
            
            # Start loading animation in a separate thread
            global loading_flag
            loading_flag = True
            loading_thread = threading.Thread(target=loading_animation)
            loading_thread.start()

            # Generate response
            response = model.generate(user_input)
            
            # Stop loading animation and display the response
            loading_flag = False
            loading_thread.join()
            print("\r" + " " * 30, end="\r")  # Clear the loading line
            print("Chatbot:", response)

    except FileNotFoundError:
        print(f"Model file not found at {model_path}. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main entry point
if __name__ == "__main__":
    loading_flag = False
    mental_health_chat()
