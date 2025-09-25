#!/usr/bin/env python3.9

import speech_recognition as sr

def listen_for_task():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            task = r.recognize_google(audio, language='en-in')
            print(f"You said: {task}")
            return task
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(f"{task}\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            if tasks:
                print("Your tasks are:")
                for task in tasks:
                    print(f"- {task}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("The tasks file was not found.")

def delete_task(task):
    pass

def main():
    # Add a stop clause to stop listening
    while True:
        task = listen_for_task()
        # confirm if what was said was correct
        if task:
            add_task(task)
            print("Task added!")
        
        # View tasks every 5 additions
        if input("Do you want to view tasks? (yes/no): ").lower() == "yes":
            view_tasks()
            

if __name__ == "__main__":
    main()