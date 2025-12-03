# DeepSeek AI Application Installation Guide

## Overview
This package contains an AI application powered by DeepSeek API with a settings interface for API key configuration.

## Installation Methods

### Method 1: Using the Install Script (Windows)
1. Make sure you have Python 3.7 or higher installed
2. Run the `install.bat` file as administrator
3. Follow the prompts to complete the installation

### Method 2: Manual Installation
1. Copy all files to a directory (e.g., `C:\Program Files\DeepSeekAI`)
2. Install dependencies: `pip install -r requirements.txt`
3. Create shortcuts to `main.py` and `setup_gui.py` as needed

### Method 3: Using PyInstaller to Create Executables
1. Install PyInstaller: `pip install pyinstaller`
2. Create the settings executable: `pyinstaller --name=DeepSeekAI_Settings --windowed setup_gui.py`
3. Create the main application executable: `pyinstaller --name=DeepSeekAI --windowed main.py`
4. The executables will be in the `dist` folder

## Using the Application

### Setting up Your API Key
1. Run the "DeepSeekAI_Settings" application
2. Enter your DeepSeek API key in the settings window
3. Adjust other parameters as needed (model, temperature, max tokens)
4. Click "Save Settings"

### Running the AI Application
1. Run the main "DeepSeekAI" application
2. Start chatting with the AI

## Configuration
The application stores settings in a configuration file located at:
`%USERPROFILE%\.deepseek_ai\config.ini`

This file contains:
- Your API key
- Selected model
- Temperature setting
- Max tokens setting

## Creating a Professional Installer
To create a professional Windows installer:
1. Install NSIS (Nullsoft Scriptable Install System)
2. Use the provided `installer.nsi` script
3. Run: `makensis installer.nsi`

This will create a professional installer executable that users can run to install the application.

## Uninstallation
To uninstall, simply delete the installation directory and remove any shortcuts you created. The configuration file will remain in `%USERPROFILE%\.deepseek_ai\` if you wish to keep your settings.