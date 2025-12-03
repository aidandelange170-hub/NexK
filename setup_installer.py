"""
Setup script for DeepSeek AI application installer
This creates a distributable package with a settings interface for API key configuration
"""

from setuptools import setup
import os

# Read the long description from README
long_description = """
# DeepSeek AI Application

A powerful AI application powered by DeepSeek API. This application provides:
- Chat interface with the DeepSeek AI model
- Settings panel to configure your API key
- Configurable parameters (model, temperature, max tokens)

## Installation

Run the installer and follow the prompts to install the application.

## Usage

After installation:
1. Run the Settings application to enter your DeepSeek API key
2. Launch the main AI application to start chatting with the AI
"""

setup(
    name="DeepSeekAI",
    version="1.0.0",
    author="AI Solutions",
    author_email="info@example.com",
    description="AI application powered by DeepSeek API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepseek-ai-app/deepseek-ai",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=[],
    install_requires=[
        "openai>=1.0.0",
        "tkinter",  # Usually comes with Python
        "configparser",
        "pathlib"
    ],
    entry_points={
        'console_scripts': [
            'deepseek-ai=main:main',
        ],
        'gui_scripts': [
            'deepseek-ai-settings=setup_gui:main',
        ]
    },
    python_requires=">=3.7",
    include_package_data=True,
    data_files=[
        ('.', ['main.py', 'setup_gui.py', 'requirements.txt', 'README.md'])
    ]
)