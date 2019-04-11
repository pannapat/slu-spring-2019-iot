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

r = sr.Recognizer()

# harvard = sr.AudioFile('audio_files/harvard.wav')
# with harvard as source:
#     audio = r.record(source)
# recognize_speech_from_mic(recog, m)

# print(type(audio))
# print(r.recognize_sphinx(audio))
# print(r.recognize_google(audio))
#
# obtain audio from the microphone
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)
    try:
        print("(recognize_google) Google thinks you said '" + r.recognize_google(audio) + "'")
        # print("(recognize_sphinx) Google thinks you said '" + r.recognize_sphinx(audio) + "'")
        # print("(recognize_bing) Google thinks you said '" + r.recognize_bing(audio) + "'")
        # print("(recognize_google_cloud) Google thinks you said '" + r.recognize_google_cloud(audio) + "'")
        # print("(recognize_ibm) Google thinks you said '" + r.recognize_ibm(audio) + "'")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")

    # recognize speech using Sphinx
try:
    print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))