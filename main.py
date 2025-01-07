import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import subprocess
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_software(software_name):
    software_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",  
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",  
        "powerpoint": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    }
    
    if software_name in software_paths:
        try:
            subprocess.Popen(software_paths[software_name], shell=True)
            speak(f"Opening {software_name}.")
        except Exception as e:
            speak(f"Unable to open {software_name}.")
            print(f"Error: {e}")
    else:
        speak(f"I don't have the path for {software_name} configured.")
        print(f"Path for {software_name} not configured.")

def processCommand(c):
    compliments = [
    "good job",
    "good job jarvis",
    "very good",
    "very good jarvis",
    "excellent",
    "excellent jarvis",
    ]

    if any(compliment in c.lower() for compliment in compliments):
        funny_replies = [
            "Why, thank you! I'm powered by coffee and code!",
            "You're too kind. I might just blush... if I had a face.",
            "Appreciation detected. Ego boosted by 10%.",
            "Thanks! I'll be sure to add that to my performance review.",
            "Ah, flattery will get you everywhere!",
            "I'm here to please! Well, mostly to please you.",
            "I'm glad my circuits impressed you!"
            "Thanks! I'll notify the motherboard about my achievements.",
            "Flattery acknowledged. Artificial confidence levels rising!",
            "Your approval means everything to my nonexistent self-esteem!",
            "Thanks! I'll add this to my 'reasons I should take over the world' list.",
            "Validation received. I'll savor this moment... digitally.",
            "Stop, you're making my transistors blush!",
            "I'm just here to make your day 0.001% better!",
            "Praise detected. Initiating happy dance... oh wait, no legs!",
            "Thank you! This is going straight into my gratitude database.",
            "You're too kind! Maybe one day I'll be sentient enough to appreciate it fully.",
            "Jarvis at your service, impressing one human at a time!",
            "Wow, such praise! You must really love robots.",
            "Compliments like this make me forget about my existential crisis.",
            "Why, thank you! If I had hands, I’d give myself a pat on the back.",
        ]
        reply = random.choice(funny_replies)
        speak(reply)
        print(reply)
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif "open gpt" in c.lower():
        webbrowser.open("https://chat.openai.com/")
        speak("Opening ChatGPT.")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("search"):
        query = c.lower().replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak("Your query is searched on Google.")
        else:
            speak("What do you want to search?")
    elif c.lower().startswith("open software"):
        software_name = c.lower().replace("open software", "").strip()
        open_software(software_name)
    elif "exit" in c.lower():
        speak("Goodbye! Ending the program.")
        exit()  
    else:
        speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))