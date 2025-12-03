from main import DeepSeekAI

def demonstrate_features():
    """
    Demonstrates various features of the DeepSeek AI
    """
    print("Initializing DeepSeek AI...")
    ai = DeepSeekAI()
    
    print("\n" + "="*50)
    print("DEEPSEEK AI DEMONSTRATION")
    print("="*50)
    
    # Example 1: Simple chat
    print("\n1. CHAT EXAMPLE:")
    print("User: Hello, can you introduce yourself?")
    response = ai.chat("Hello, can you introduce yourself?")
    print(f"AI: {response}")
    
    # Example 2: Text generation
    print("\n2. TEXT GENERATION EXAMPLE:")
    print("User: Write a short poem about AI")
    response = ai.generate_text("Write a short poem about AI")
    print(f"AI: {response}")
    
    # Example 3: Question answering
    print("\n3. QUESTION ANSWERING EXAMPLE:")
    print("User: What are the benefits of artificial intelligence?")
    response = ai.chat("What are the benefits of artificial intelligence?")
    print(f"AI: {response}")
    
    # Example 4: Creative writing
    print("\n4. CREATIVE WRITING EXAMPLE:")
    print("User: Write a short story about a robot learning to understand humans")
    response = ai.generate_text("Write a short story about a robot learning to understand humans", max_tokens=500)
    print(f"AI: {response}")
    
    print("\n" + "="*50)
    print("DEMONSTRATION COMPLETE")
    print("="*50)

if __name__ == "__main__":
    try:
        demonstrate_features()
    except ValueError as e:
        print(f"Error: {e}")
        print("Make sure your DEEPSEEK_API_KEY is set in the environment.")
    except Exception as e:
        print(f"Unexpected error: {e}")