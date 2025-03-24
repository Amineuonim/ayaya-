import tkinter as tk
import subprocess
from tkinter import scrolledtext, filedialog, messagebox
from models import ModelBibi
from core import OllamaCore

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        print("Selected file:", file_path)


def send_message():
    user_input = entry.get()
    if user_input.strip():
        chat_window.config(state=tk.NORMAL)  # Enable editing
        chat_window.insert(tk.END, f"You: {user_input}\n", "user")
        response = lamia.run(user_input)
        chat_window.insert(tk.END, f"Bot: {response}\n", "bot")
        chat_window.config(state=tk.DISABLED)  # Disable editing
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("ayaya!")
root.geometry("600x700")

lamia =OllamaCore() 

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10, fill="both", expand=True, padx=10)
chat_window.config(width=1)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

# Main frame for input + buttons
in_frame = tk.Frame(root)
in_frame.pack()

upper_frame = tk.Frame(root)
bibi= ModelBibi(lamia,upper_frame)
upper_frame.pack()

bibi.get_btn().pack()


# Text input area
entry = tk.Entry(in_frame, font=("Arial", 12), width=40)
entry.pack(pady=5)

# Send button
send_button = tk.Button(
    in_frame,
    bg="#FF69B4",    
    fg="#FFF0F5", 
    text="Send", 
    command=send_message
)
send_button.pack(side="left")

# Upload button
upload_button = tk.Button(
    in_frame,
    bg="#FF69B4",    
    fg="#FFF0F5", 
    text="Upload PDF", 
    command=open_file
)
upload_button.pack(side="left")

# Run application
root.mainloop()
