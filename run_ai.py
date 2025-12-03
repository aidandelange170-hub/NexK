"""
Simple launcher for the DeepSeek AI application
This script can be used to run the main application
"""
import sys
import os
from pathlib import Path

# Add the current directory to the path so we can import the modules
sys.path.insert(0, str(Path(__file__).parent))

def main():
    try:
        # Import and run the main application
        from main import main as ai_main
        ai_main()
    except ImportError as e:
        print(f"Error importing main application: {e}")
        print("Make sure all required files are in the same directory.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()