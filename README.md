# DeepSeek AI Application

This is an AI-powered application that uses the DeepSeek API to provide conversational AI capabilities.

## Features

- Chat with an AI assistant powered by DeepSeek models
- Text generation based on prompts
- Easy-to-use command-line interface
- Configurable parameters (temperature, max tokens, etc.)

## Prerequisites

- Python 3.7 or higher
- A DeepSeek API key

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Get your DeepSeek API key from [DeepSeek](https://www.deepseek.com/) (if available) or through their API access program

## Configuration

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit the `.env` file and add your DeepSeek API key:

```bash
DEEPSEEK_API_KEY=your_actual_api_key_here
```

## Usage

Run the application:

```bash
python main.py
```

The application will start an interactive chat session where you can type messages and receive responses from the AI.

## Example Usage

```
You: Hello, how are you?
AI: I'm an AI assistant created by DeepSeek. I don't have feelings, but I'm functioning properly and ready to help you!

You: What can you do?
AI: I can answer questions, help with writing, explain concepts, and much more. What would you like to know?
```

## Customization

You can modify the following parameters in the code:
- `model`: The model to use (default: "deepseek-chat")
- `max_tokens`: Maximum number of tokens in the response (default: 1000)
- `temperature`: Controls randomness (default: 0.7)

## API Models

The application uses the `deepseek-chat` model by default. DeepSeek offers various models that you can experiment with.

## License

This project is licensed under the terms provided in the LICENSE file.