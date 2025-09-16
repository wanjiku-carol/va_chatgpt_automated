#!/usr/bin/env python3.9

import time
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines

def callback(recognizer, audio):
    try:
        print("You said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition")



r = sr.Recognizer()
def listen_to_user():
    """
    This function contains the script for listening to user 
    input for the key words that are supplied for the todo application.
    :param: There are no parameters.
    :return: The text translated from the audio retreived through the microphone.
    """
    print("Listening ...")
    with sr.Microphone() as source:
        print("Microphone on..")
        r.adjust_for_ambient_noise(source, duration=0.10)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if text != "stop":
            return text
    stop_listening = r.listen_in_background(source, callback)
    return stop_listening


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



except_list = [
    "add new task",
    "list my tasks",
    "yes",
    "no"  
]

commands_dict = {
        "add_task_command": "add new task",
        "list_tasks": "list my tasks"
    }
  
def add_task(task):
    """
    A helper function that adds tasks to a dictionary to maintiain order 
    :param task: The tasks retreived from the user speaking on the microphone.
    :return added_tasks: A dictionary containing the tasks as the values and 
    incrementing numbers as the keys to maintain order.
    """
    count = 1
    tasks = {}
    for key, val in tasks.items():
        key = count
        val = task
        tasks[key] = val
        key += 1
    return tasks


def add_new_task(new_task): 
    """
    TODO: USE THE WHILE OUTSIDE THE FUNCTION
    The main function that receives todo tasks, saves them in the dictionary, and lists all of the tasks if asked to.
    The key words that trigger these actions are in the commands_dict.
    :param None: The tasks retreived from the user speaking on the microphone.
    :return say_something: Verbal responses from the virtual assistant affirming an added task or listing added tasks 
    """
    tasks = add_task(task=None)
    time.sleep(0.2)
    print("Adding new task ...")
    
    if len(tasks) == 0:
        speak("There are no tasks in the todo list.")
    
    speak(f"Would you like to add {new_task} to the todo list?")
    confirm = listen_to_user()
    if confirm == "yes" and new_task not in except_list:
        add_task(new_task)
        print(f'{new_task} has been added added to the todo list')
        time.sleep(0.2)
        return speak(f'{new_task} has been added to the todo list')
    elif confirm == "no":
        speak("Please renter the task")
        time.sleep(0.2)
        new_task = listen_to_user()
        add_new_task(new_task)
        


def list_tasks():
    speak("Would you like the list of tasks?")
    confirm = listen_to_user()
    
    if confirm == "yes":
        print("Retreiving ....")

        tasks = add_task(task=None)
        time.sleep(0.1)
        print("Retreiving ....")
        time.sleep(0.1)
        for key, task in tasks.items():
            key = count
            speak(f"{task}")
            print(f"{key}. {task}")
            count += 1
            time.sleep(0.3)
    elif confirm == "no":
        speak("Request cancelled. Have a nice day!")
            
        
def audio_virtual_assistant():
    
    while True:
        speak("Hello. How can I help you today?")
        command = listen_to_user()
        time.wait(0.2)
        
        if command == "stop":
            command(wait_for_stop=True)
            print("Recognition stopped.")
            break
        
        if command == commands_dict["add_task_command"]:
            speak("Which task would you like add?")
            print("Listening ...")
            time.wait(0.1)
            new_task = listen_to_user()
            add_new_task(new_task)
            
        elif command == commands_dict["list_tasks"]:
            return list_tasks()
    
if __name__ == "__main__":
    audio_virtual_assistant()