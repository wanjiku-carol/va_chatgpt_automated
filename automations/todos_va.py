import os
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Reognizer()
engine = pyttsx3.init()
file_path = os.dir



# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define funtion to recognise speech
def listen():
    with sr.Microphone() as source:
        print("Speak now ...")
        audio = r.listen(source)
    try:
        text = r.recognise_google(audio)
        lowecased_text = text.lower()
        return lowecased_text
    except:
        return None

def save_task(task, tasks):
    
    while True:
        if "stop" in task:
            break
        tasks.append(task)
    return tasks


def initialise_app():
    while True:
        tasks = []
        commands_dict = {
           rm_command: "remind me",
           cl_command:  "create a todo list"
        }
        # listens for user input
        command = listen()
        
        if len(tasks) == 0 and command is None:
            return "There are no tasks on your todo list"
        
        # remind_me_command = "remind me"
        # create_list_command = "create a todo list" 
        
        if commands_dict[rm_command] in command:
            speak("What would you like me to remind you about?")
            reminder = listen()
            speak(f"Sure, I'll remind you to {reminder} later")
            
        elif commands_dict[cl_command] in command:
            speak("What tasks do you want to add?")
            task = command
            save_task(task, tasks)

            speak("Here's your todo list")
            for i, task in enumerate(tasks):
                speak(f"{i+1}. {task}")
                
def read_article(article):
    pass