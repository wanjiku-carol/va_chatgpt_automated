#!/usr/bin/env python3.9

import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()

print("=== we got here ====")

def say_something(command):
    """
    This function contains the script that records what the user to says.
    It stays in a state of waiting for commands that will prompt todo tasks.
    The keywords will be used for 
    :param command: An audio format of words spoken by user
    :return engine.runAndWait(): an object's method for listening to audio prompts
    """
    print("=== say something function ====")
    print(f"Assistant: {command}")
    try:
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    except:
        print("Speech output not supported in Colab.")
    

# Define funtion to recognise speech
def listen_to_user():
    """
    This function contains the script for listening to user 
    input for the key words that are supplied for the todo application.
    :param: There are no parameters.
    :return: The text translated from the audio retreived through the microphone.
    """
    try:
        print("======= listening to use ====")
        with sr.Microphone() as source:
            print("Microphone on ...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognise_google(audio)
            lowercased_text = text.lower()
            return lowercased_text
    except:
        print("Speech output not supported in Colab.")

def add_task(task):
    """
    A helper function that adds tasks to a dictionary to maintiain order 
    :param task: The tasks retreived from the user speaking on the microphone.
    :return added_tasks: A dictionary containing the tasks as the values and 
    incrementing numbers as the keys to maintain order.
    """
    key = 0
    added_tasks = {}
    if task is None:
        return added_tasks
    
    for key, val in added_tasks.items():
        key += 1
        val = task
        added_tasks[key] = val
    return added_tasks

def todos_assistant():
    """
    The main function that receives todo tasks, saves them in the dictionary, and lists all of the tasks if asked to.
    The key words that trigger these actions are in the commands_dict.
    :param None: The tasks retreived from the user speaking on the microphone.
    :return say_something: Verbal responses from the virtual assistant affirming an added task or listing added tasks 
    """
    while True:
        commands_dict = {
            "remind_command": "remind me my tasks",
            "add_task_command": "add new task",
            "yes_add_task": "yes",
            "list_tasks": "list my tasks"
        }
        
        command = listen_to_user()
        # listens for user input
        if command == commands_dict["add_task_command"]:
            try:
                new_task = listen_to_user()
                add_task(new_task)
                say_something(f'{new_task} added to todo list')
            except:
                print("Speech output not supported in Colab.")
                
        if command in commands_dict["list_tasks"]:
            try:
                tasks = add_task(task=None)
                say_something("Here's your todo list")
                for key, task in enumerate(tasks):
                    say_something(f"{key}. {task}")
            except:
                print("Speech output not supported in Colab.")
            
        
def run():
    todos_assistant()
    
if __name__ == "__main__":
    run()