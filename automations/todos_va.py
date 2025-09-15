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


def say_something(command):
    """
    This function contains the script that records what the user to says.
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


def add_task(task, tasks):
    """
    A helper function that adds tasks to a dictionary to maintiain order 
    :param task: The tasks retreived from the user speaking on the microphone.
    :return added_tasks: A dictionary containing the tasks as the values and 
    incrementing numbers as the keys to maintain order.
    """
    count = 1
    
    for key, val in tasks.items():
        key = count
        val = task
        tasks[key] = val
        key += 1
    return tasks

def take_command():
    return input("You (type your command): ").lower()
# def captured_audio(command, other_commands):
#     other_commands.append(command)
#     count = 1
    
#     for comm in other_commands:
#         say_something(f"{count}: {comm}")
#         other_commands.append(command)
#         count += 1
#         time.sleep(0.2)
#     return other_commands

def todos_assistant(): 
    """
    TODO: SEPARATE THE ACTIVITIES OF SPEAKING AND SAVING
    TODO: USE CALLBACKS TO BUY TIME
    TODO: USE THE WHILE OUTSIDE THE FUNCTION
    TODO: Research pydub.silence.split_on_silence
    The main function that receives todo tasks, saves them in the dictionary, and lists all of the tasks if asked to.
    The key words that trigger these actions are in the commands_dict.
    :param None: The tasks retreived from the user speaking on the microphone.
    :return say_something: Verbal responses from the virtual assistant affirming an added task or listing added tasks 
    """
    tasks = {}
    other_commands = []
    
    while True:
        commands_dict = {
            "add_task_command": "add new task",
            "list_tasks": "list my tasks"
        }
        
        command = listen_to_user()

        time.sleep(0.1)
        if type(command) is not str:
            command(wait_for_stop=True)
            print("Recognition stopped.")
            break
        elif command == "stop":
            command(wait_for_stop=True)
            print("Recognition stopped.")
            break
        else:
            if command == commands_dict["add_task_command"]:
                new_task = listen_to_user()
                time.sleep(0.3)
                add_task(new_task, tasks)
                print(f'{new_task} has been added added to the todo list')
                time.sleep(0.2)
                say_something(f'{new_task} has been added to the todo list')

            if command == commands_dict["list_tasks"] and len(tasks) > 0:
                say_something(f"Listing tasks")
                time.sleep(0.2)
                count = 1
                for key, task in tasks.items():
                    key = count
                    say_something(f"{key}. {task}")
                    count += 1
                    time.sleep(0.2)
            # else:
            #     if command not in commands_dict.values():
            #         say_something(f"These are captured audio that weren't for the todo list")
            #         captured_audio(command, other_commands)
            #         time.sleep(0.2)
            

            
        
def run():
    todos_assistant()
    
if __name__ == "__main__":
    run()