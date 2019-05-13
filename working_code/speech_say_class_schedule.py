#!/usr/bin/python2.7


import speech_recognition as sr
import os
import utility as util


r = sr.Recognizer()

def run():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")

        r.adjust_for_ambient_noise(source, duration=3)
        print("Say \"class\" to begin")
        audio = r.listen(source)

        try:
            v_command = r.recognize_google(audio)

            if v_command == 'class':
                print("Say a course no.")
                os.system("espeak 'Say a course number'")

                audio2 = r.listen(source)
                course_id_str = r.recognize_google(audio2)
                print(course_id_str)
                try:
                    course_id = int(course_id_str)
                    say_class_schedule(course_id)
                except ValueError:
                    print("I could not recognize any course number.")
            else:
                print("I did not recognize any commands I know")

        except sr.UnknownValueError:
            print("I could not understand audio")
        
def say_class_schedule(id):
    schedule = util.get_class_schedule(id);
    if schedule == {}:
        response = "Sorry. The course cannot be found"
        print(response)
        os.system("espeak '"+response+"'");
    else:
        response = "The course number " + str(id) + " has class on " + schedule['hours'] + ". Every " + schedule['days'] + ". Lectured by professor " + schedule['professor']
        print(response)

        os.system("espeak '"+response+"'")

if __name__ == "__main__":
    run()


# INPUT: Say "hello" > Say "class" > Say <course no.> e.g. 5300
# OUTPUT: course schedule
