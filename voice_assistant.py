import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening. Please say something.")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError:
            speak("There seems to be a problem with the speech recognition service.")
        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
        return None

# Process commands
def process_command(command):
    if "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}.")
    elif "open" in command and "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
    elif "weather" in command:
        speak("Fetching weather details is not set up in this demo, but it can be added!")
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False
    else:
        speak("Sorry, I can't handle that command yet.")
    return True

# Main function
def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if not process_command(command):
                break

# Run the assistant
if __name__ == "__main__":
    main()

