#!/usr/bin/python2.7
# works with Python2.7.x
# import speech_recognition as sr
# from guessing_game import recognize_speech_from_mic
#
# print (sr._version_)
#
# recog = sr.Recognizer()
#
# # print(recog.recognize_sphinx())
#
# # m = sr.Microphone()

# USE ESPEAK TO MAKE RUN THE SPEAKER

import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()
engine = pyttsx3.init() # may not need this because we change to use espeak
WAKE_UP_WORD = 'hello'
def run():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")

        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        os.system("espeak 'Say " + WAKE_UP_WORD + " to wake me up...'")

        try:
            word = r.recognize_google(audio)
            if (word == WAKE_UP_WORD):
                while (1):
                    os.system("espeak 'Listening for commands...'")
                    listen(source)
            else:
                os.system("espeak 'I didnt hear any wake-up word.'")
        except sr.UnknownValueError:
            os.system("espeak 'I'm sorry. I can't understand that.'")
            

def listen(source):

    print("Listen for a command...")
    
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source)
    v_command = ''
    try:
        v_command = r.recognize_google(audio)
        print("(recognize_google) Google thinks you said '" + v_command + "'")

        # print("(recognize_sphinx) Google thinks you said '" + v_command + "'")
        # print("(recognize_bing) Google thinks you said '" + v_command + "'")
        # print("(recognize_google_cloud) Google thinks you said '" + v_command + "'")
        # print("(recognize_ibm) Google thinks you said '" + v_command + "'")
        # extract_voice_command()
    except sr.UnknownValueError:
        print("I could not understand audio")

    try:
        print("I thinks you said '" + v_command + "'")
        engine.say("I heard you said " + v_command)
    except sr.UnknownValueError:
        print("I could not understand audio")
        engine.say("I can't recognize any commands")
    except sr.RequestError as e:
        print("I error; {0}".format(e))
        engine.say("There's an error")
    
    engine.runAndWait()


def speak():
    engine.say("hello, the engine is working")

