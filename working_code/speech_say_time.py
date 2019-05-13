import speech_recognition as sr
import os
import time

r = sr.Recognizer()

def run():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")

        r.adjust_for_ambient_noise(source, duration=2)
        print("I'm listening")
        audio = r.listen(source)

        try:
            v_command = r.recognize_google(audio)
            print("(recognize_google) Google thinks you said '" + v_command + "'")

            if v_command == 'time':
                say_time()

        except sr.UnknownValueError:
            print("I could not understand audio")

        # try:
        #     print("I heard you said '" + v_command + "'")
        # except sr.UnknownValueError:
        #     print("I can't recognize any commands")
        # except sr.RequestError as e:
        #     print("There's an error; {0}".format(e))
        
def say_time():
    currenttime = time.strftime("%A %B %d, %Y %I:%M %p", time.localtime()) # Thursday 25 Apr 2019 12:04 PM'
    os.system("espeak 'Today is " + currenttime + "'")

if __name__ == "__main__":
    run()

# hello > class > listen to the cource no. > say schedule
