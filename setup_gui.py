import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import configparser
import subprocess
import sys
from pathlib import Path

class DeepSeekAIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepSeek AI - Settings")
        self.root.geometry("500x400")
        
        # Create config directory if it doesn't exist
        self.config_dir = Path.home() / ".deepseek_ai"
        self.config_dir.mkdir(exist_ok=True)
        
        self.config_file = self.config_dir / "config.ini"
        self.load_config()
        
        self.create_widgets()
        self.load_settings()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # API Key section
        ttk.Label(main_frame, text="DeepSeek API Key:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.api_key_var = tk.StringVar()
        api_key_frame = ttk.Frame(main_frame)
        api_key_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.api_key_entry = ttk.Entry(api_key_frame, textvariable=self.api_key_var, show="*", width=50)
        self.api_key_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        self.show_api_key_var = tk.BooleanVar()
        ttk.Checkbutton(api_key_frame, text="Show", variable=self.show_api_key_var, 
                       command=self.toggle_api_key_visibility).grid(row=0, column=1, padx=(5, 0))
        
        # Model selection
        ttk.Label(main_frame, text="Model:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky=tk.W, pady=(15, 5))
        
        self.model_var = tk.StringVar(value="deepseek-chat")
        model_options = ["deepseek-chat", "deepseek-coder"]
        self.model_combo = ttk.Combobox(main_frame, textvariable=self.model_var, values=model_options, state="readonly")
        self.model_combo.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Temperature setting
        ttk.Label(main_frame, text="Temperature:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky=tk.W, pady=(15, 5))
        
        self.temp_var = tk.DoubleVar(value=0.7)
        self.temp_scale = ttk.Scale(main_frame, from_=0.0, to=2.0, variable=self.temp_var, orient=tk.HORIZONTAL)
        self.temp_scale.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.temp_label = ttk.Label(main_frame, textvariable=self.temp_var)
        self.temp_label.grid(row=5, column=1, padx=(5, 0))
        
        # Max tokens setting
        ttk.Label(main_frame, text="Max Tokens:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky=tk.W, pady=(15, 5))
        
        self.max_tokens_var = tk.IntVar(value=1000)
        self.max_tokens_spin = ttk.Spinbox(main_frame, from_=100, to=4096, increment=100, 
                                          textvariable=self.max_tokens_var, width=10)
        self.max_tokens_spin.grid(row=7, column=0, sticky=tk.W, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)
        
        self.save_btn = ttk.Button(button_frame, text="Save Settings", command=self.save_settings)
        self.save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.test_btn = ttk.Button(button_frame, text="Test API Connection", command=self.test_api_connection)
        self.test_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.launch_btn = ttk.Button(button_frame, text="Launch AI App", command=self.launch_ai_app)
        self.launch_btn.pack(side=tk.LEFT)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def load_config(self):
        self.config = configparser.ConfigParser()
        if self.config_file.exists():
            self.config.read(self.config_file)
        else:
            # Create default config
            self.config['DEFAULT'] = {
                'api_key': '',
                'model': 'deepseek-chat',
                'temperature': '0.7',
                'max_tokens': '1000'
            }
    
    def load_settings(self):
        self.api_key_var.set(self.config.get('DEFAULT', 'api_key', fallback=''))
        self.model_var.set(self.config.get('DEFAULT', 'model', fallback='deepseek-chat'))
        self.temp_var.set(float(self.config.get('DEFAULT', 'temperature', fallback='0.7')))
        self.max_tokens_var.set(int(self.config.get('DEFAULT', 'max_tokens', fallback='1000')))
    
    def save_settings(self):
        self.config['DEFAULT']['api_key'] = self.api_key_var.get()
        self.config['DEFAULT']['model'] = self.model_var.get()
        self.config['DEFAULT']['temperature'] = str(self.temp_var.get())
        self.config['DEFAULT']['max_tokens'] = str(self.max_tokens_var.get())
        
        with open(self.config_file, 'w') as f:
            self.config.write(f)
        
        messagebox.showinfo("Success", "Settings saved successfully!")
    
    def toggle_api_key_visibility(self):
        if self.show_api_key_var.get():
            self.api_key_entry.config(show="")
        else:
            self.api_key_entry.config(show="*")
    
    def test_api_connection(self):
        try:
            # Import the AI class from main.py
            sys.path.append(str(Path(__file__).parent))
            from main import DeepSeekAI
            
            # Create a temporary instance with the settings
            ai = DeepSeekAI(
                api_key=self.api_key_var.get(),
                model=self.model_var.get(),
                temperature=self.temp_var.get(),
                max_tokens=self.max_tokens_var.get()
            )
            
            # Test the connection
            response = ai.chat("Hello, this is a test message to verify the API connection.", max_tokens=50)
            
            if response:
                messagebox.showinfo("Success", "API connection successful!")
            else:
                messagebox.showerror("Error", "API connection failed.")
        except Exception as e:
            messagebox.showerror("Error", f"API connection failed: {str(e)}")
    
    def launch_ai_app(self):
        try:
            # Save settings first
            self.save_settings()
            
            # Launch the main AI application
            subprocess.Popen([sys.executable, str(Path(__file__).parent / "main.py")])
            messagebox.showinfo("Success", "AI application launched!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch AI application: {str(e)}")

def main():
    root = tk.Tk()
    app = DeepSeekAIGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()