
import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
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

chatbot = Chat(pairs, reflections)

# Start conversation
def start_chatbot():
    print("Chatbot: Hello! I am a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
