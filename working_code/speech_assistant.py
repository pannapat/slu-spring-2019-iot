import speech_recognition as sr
import os
import time
import led as l
import utility as util
from espeak import espeak

wake_word = 'hello'
keywords = ['time', 'class']

r = sr.Recognizer()
l.setup()

def run():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")

        r.adjust_for_ambient_noise(source, duration=2)
        while(True):
            l.both_off()
            l.green()
            audio = r.listen(source)
            l.both_off()
            l.red()
            try:
                v_command = r.recognize_google(audio)
                print("(recognize_google) Google thinks you said '" + v_command + "'")

                if wake_word in v_command:
                    espeak.synth("hi, I'm listening")
                    l.both_off()
                    l.cyan()
                    audio2 = r.listen(source)
                    l.both_off()
                    l.red()
                    try:
                        v_command2 = r.recognize_google(audio2)
                        print("(recognize_google) Google thinks you said '" + v_command + "'")
                        
                        if keywords[0] in v_command2:
                            say_time()
                            break
                        if keywords[1] in v_command2:
                            print("Say a course no.")
                            espeak.synth('Say a course number')
                            l.both_off()
                            l.cyan()
                            audio3 = r.listen(source)
                            l.both_off()
                            l.red()
                            course_id_str = r.recognize_google(audio3)
                            print(course_id_str)
                            try:
                                course_id = int(course_id_str)
                                say_class_schedule(course_id)
                            except ValueError:
                                print("I could not recognize any course number.")
                            break
                        
                    except sr.UnknownValueError:
                        print("I could not understand audio")

            except sr.UnknownValueError:
                print("I could not understand audio")

def say_time():
    currenttime = time.strftime("%A %B %d, %Y %I:%M %p", time.localtime()) # Thursday 25 Apr 2019 12:04 PM'
    os.system("espeak 'Today is " + currenttime + "'")

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
