import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DeepSeekAI:
    def __init__(self):
        # Set up the DeepSeek API key and base URL
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
        
        # Configure the OpenAI client for DeepSeek API
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )
    
    def chat(self, message, model="deepseek-chat", max_tokens=1000, temperature=0.7):
        """
        Send a message to the DeepSeek API and return the response
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": message}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error occurred: {str(e)}"
    
    def generate_text(self, prompt, model="deepseek-chat", max_tokens=1000, temperature=0.7):
        """
        Generate text based on the given prompt
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error occurred: {str(e)}"

def main():
    print("Initializing DeepSeek AI...")
    
    try:
        ai = DeepSeekAI()
        print("DeepSeek AI initialized successfully!")
        print("Type 'quit' to exit the program.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            if user_input.strip() == "":
                continue
            
            print("AI: ", end="")
            response = ai.chat(user_input)
            print(response)
            print()
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure you have set the DEEPSEEK_API_KEY environment variable.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()