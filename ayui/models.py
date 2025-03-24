import tkinter as tk
import subprocess
from tkinter import messagebox
from core import OllamaCore

class ModelBibi:  # Class names should follow PascalCase

    def __init__(self, ollamacore, parent_frame):
        self.llamia = ollamacore
        self.parent = parent_frame
        self.models_frame = tk.Frame(self.parent)

        self.open_btn = tk.Button(self.models_frame, text="models", command=self.open_menu)
        self.open_btn.pack(side="left")

        self.list_frame = tk.Frame(self.models_frame)
        self.close_btn = tk.Button(self.list_frame, text="close", bg="#FFFFFF", command=self.close)
        self.close_btn.pack()
        

    def get_installed_models(self):
        try:
            result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
            models = [line.split()[0] for line in result.stdout.strip().split("\n") if line]
            return models
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to retrieve models. Is Ollama installed and running?")
            return []

    def open_menu(self):
        models = self.get_installed_models()
        for widget in self.list_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.close_btn:
                widget.destroy()

        self.list_frame.pack()
        self.close_btn.pack()
        for model in models[1:]:
            b = tk.Button(self.list_frame, text=model, command=lambda m=model: self.llamia.set_model(m))
            b.pack()

    def close(self):
        self.list_frame.pack_forget()

    def get_btn(self):
        return self.models_frame
