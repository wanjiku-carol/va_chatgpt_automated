#!/usr/bin/env python3.9

import time
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines

def callback(recognizer, audio):
    try:
        print("You said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError as e:
        return(f"Could not understand audio. \n Returned Error:{e}") 
    except sr.RequestError as e:
        return(f"Could not request results from Google Speech Recognition.\n Returned Error: {e}")


r = sr.Recognizer()

def listen_to_user():
    """
    This function contains the script for listening to user 
    input for the key words that are supplied for the todo application.
    :param: There are no parameters.
    :return: The text translated from the audio retreived through the microphone.
    """
    with sr.Microphone() as source:
        print("Microphone on..")
        r.adjust_for_ambient_noise(source, duration=0.10)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        
        stop_listening = r.listen_in_background(source, callback)
        if text.lower() == "stop":
            stop_listening
    
    return text.lower() # Small delay to avoid busy-waiting


def speak(command):
    """
    It contains the script that captures what the user to says.
    It stays in a state of waiting for commands that will prompt todo tasks.
    The keywords will be used for 
    :param command: An audio format of words spoken by user
    :return engine.runAndWait(): an object's method for listening to audio prompts
    """
    try:
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    except:
        print("Speech output not supported in Colab.")
        return



except_list = [
    "add new task",
    "list my tasks",
    "yes",
    "no"  
]

commands_dict = {
        "add_task_command": "add new task",
        "list_tasks": "list my tasks",
        "no_tasks": "There are no tasks in the todo list.",
        "greetings": "Hello. How can I help you today?"
    }
  
def add_task(task):
    """
    A helper function that adds tasks to a dictionary to maintiain order 
    :param task: The tasks retreived from the user speaking on the microphone.
    :return added_tasks: A dictionary containing the tasks as the values and 
    incrementing numbers as the keys to maintain order.
    """
    
    pass

_tasks = {}

def add_new_task(): 
    """
    TODO: USE THE WHILE OUTSIDE THE FUNCTION
    The main function that receives todo tasks, saves them in the dictionary, and lists all of the tasks if asked to.
    The key words that trigger these actions are in the commands_dict.
    :param None: The tasks retreived from the user speaking on the microphone.
    :return say_something: Verbal responses from the virtual assistant affirming an added task or listing added tasks 
    """
    
    time.sleep(0.2)
    print("Adding new task ...")
    new_task = listen_to_user()
    
    if new_task not in except_list:
        count = 1
        for key, val in _tasks.items():
            key = count
            val = new_task
            _tasks[key] = val
            print(f'{new_task} has been added added to the todo list')
            count += 1
            time.sleep(0.1)
            print(f'{new_task} has been added to the todo list')
        return _tasks
    else:
        return print("Speech output not supported in Colab.")
        


def list_tasks():
    print("Retreiving ....")
    if len(_tasks) == 0:
        return print("There are no tasks in the todo list")
    for key, task in _tasks.items():
        key = count
        speak(f"{task}")
        print(f"{key}. {task}")
        count += 1
        time.sleep(0.1)
    return print("That's all. Best of luck")

        
def audio_virtual_assistant():
    
    command = listen_to_user()
    
    while True:     
        time.sleep(0.1)
        
        if command == "stop":
            break
        elif command == commands_dict["add_task_command"]:
            add_new_task()    
        elif command == commands_dict["list_tasks"]:
            return list_tasks()
        else:
            print("Speech output not supported in Colab.")

    
if __name__ == "__main__":
    audio_virtual_assistant()