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


import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
WAKE_UP_WORD = 'hello'
def run():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")

        r.adjust_for_ambient_noise(source, duration=2)
        print('Waiting for a wake-up word ("'+WAKE_UP_WORD +")...')
        audio = r.listen(source)

        try:
            word = r.recognize_google(audio)
            if (word == WAKE_UP_WORD):
                while (1):
                    "Listening for commands..."
                    listen(source)
            else:
                print("I didnt hear any wake-up word.")
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")


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