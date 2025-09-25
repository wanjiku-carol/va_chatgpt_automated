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
