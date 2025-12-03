import os
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'packages': ['tkinter', 'configparser', 'pathlib'],
    'excludes': [],
    'include_files': []  # Add any additional files here if needed
}

# Define executables
executables = [
    Executable(
        'setup_gui.py',
        target_name='DeepSeekAI_Setup.exe',
        base='Win32GUI',  # Use 'Win32GUI' for Windows GUI application
        icon=None  # Add path to icon file if available
    ),
    Executable(
        'main.py',
        target_name='DeepSeekAI.exe',
        base='Win32GUI',
        icon=None
    )
]

setup(
    name='DeepSeekAI',
    version='1.0.0',
    description='AI application powered by DeepSeek API',
    options={'build_exe': build_options},
    executables=executables
)