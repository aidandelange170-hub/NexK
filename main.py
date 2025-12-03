import os
import openai
import configparser
from pathlib import Path

class DeepSeekAI:
    def __init__(self, api_key=None, model=None, temperature=None, max_tokens=None):
        # Load settings from config file if not provided
        config = self.load_config()
        
        # Use provided parameters or fall back to config values
        self.api_key = api_key or config.get('DEFAULT', 'api_key', fallback='')
        if not self.api_key:
            raise ValueError("No API key provided. Please set your API key in the settings.")
        
        self.model = model or config.get('DEFAULT', 'model', fallback='deepseek-chat')
        self.temperature = temperature or float(config.get('DEFAULT', 'temperature', fallback='0.7'))
        self.max_tokens = max_tokens or int(config.get('DEFAULT', 'max_tokens', fallback='1000'))
        
        # Configure OpenAI client for DeepSeek
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )
    
    def load_config(self):
        """Load configuration from the config file."""
        config = configparser.ConfigParser()
        config_dir = Path.home() / ".deepseek_ai"
        config_file = config_dir / "config.ini"
        
        if config_file.exists():
            config.read(config_file)
        else:
            # Create default config
            config['DEFAULT'] = {
                'api_key': '',
                'model': 'deepseek-chat',
                'temperature': '0.7',
                'max_tokens': '1000'
            }
        
        return config
    
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
            # Use the configured model, temperature, and max_tokens from the config
            response = ai.chat(user_input, model=ai.model, temperature=ai.temperature, max_tokens=ai.max_tokens)
            print(response)
            print()
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure you have set your API key in the settings.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()