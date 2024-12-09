import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Ensure NLTK components are available
nltk.download('punkt')

# Define conversation pairs
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help you?"]),
    (r"what is your name?", ["I'm a chatbot. You can call me Chatbot!"]),
    (r"how are you?", ["I'm just a bot, but I'm here to help you! How can I assist?"]),
    (r"what can you do?", ["I can answer your questions, assist with basic tasks, and keep you company!"]),
    (r"bye|exit|quit", ["Goodbye! Have a great day!", "See you later! Take care!"]),
    (r"my name is (.*)", ["Nice to meet you, %1! How can I assist you?"]),
    (r"i need help with (.*)", ["Sure, I can help with %1. Could you tell me more?"]),
    (r"(.*) created you?", ["I was created by a Python developer using NLP techniques!"]),
    (r"(.*)", ["I'm not sure I understand that. Could you rephrase or ask something else?"])
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Create a Tkinter GUI
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_display.place(x=10, y=10, width=480, height=450)
        self.chat_display.configure(state="disabled")  # Disable editing

        # User input area
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.place(x=10, y=480, width=400, height=30)
        self.entry.bind("<Return>", self.process_input)  # Bind Enter key to send message

        # Send button
        self.send_button = tk.Button(root, text="Send", font=("Arial", 12), command=self.process_input)
        self.send_button.place(x=420, y=480, width=70, height=30)

        # Add exit button
        self.exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
        self.exit_button.place(x=10, y=520, width=480, height=30)

    def process_input(self, event=None):
        # Get user input
        user_input = self.entry.get().strip()
        if not user_input:
            return

        # Display user input in chat
        self.update_chat("You", user_input)
        self.entry.delete(0, tk.END)  # Clear the input box

        # Check if the user wants to exit
        if user_input.lower() in ["bye", "exit", "quit"]:
            self.update_chat("Chatbot", "Goodbye! Have a great day!")
            self.root.quit()
            return

        # Get chatbot response
        response = chatbot.respond(user_input)
        self.update_chat("Chatbot", response)

    def update_chat(self, speaker, message):
        self.chat_display.configure(state="normal")  # Enable editing
        self.chat_display.insert(tk.END, f"{speaker}: {message}\n")  # Add the message
        self.chat_display.see(tk.END)  # Scroll to the bottom
        self.chat_display.configure(state="disabled")  # Disable editing again

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
