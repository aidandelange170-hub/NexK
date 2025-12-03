import os
import subprocess
import sys

def create_executables():
    """Create executables for the DeepSeek AI application using PyInstaller."""
    
    # Create the settings executable
    print("Creating settings executable...")
    subprocess.run([
        sys.executable, '-m', 'PyInstaller',
        '--name=DeepSeekAI_Settings',
        '--windowed',  # For GUI application
        '--add-data=main.py;.',  # Include main.py in the executable
        '--add-data=requirements.txt;.',
        '--add-data=README.md;.',
        'setup_gui.py'
    ])
    
    # Create the main AI application executable
    print("Creating main AI application executable...")
    subprocess.run([
        sys.executable, '-m', 'PyInstaller',
        '--name=DeepSeekAI',
        '--windowed',  # For GUI application
        'main.py'
    ])
    
    print("Executables created successfully in the 'dist' folder!")

if __name__ == "__main__":
    create_executables()