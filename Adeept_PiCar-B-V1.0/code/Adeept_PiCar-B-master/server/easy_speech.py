#!/usr/bin/python3
import speech_recognition as sr

v_command = ''
def run():
    global v_command
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index =2,sample_rate=48000) as source:
        r.record(source,duration=2)
        #r.adjust_for_ambient_noise(source)
        print("Command?")
        audio = r.listen(source)

    try:
        v_command = r.recognize_sphinx(audio,
        keyword_entries=[('forward',1.0),('backward',1.0),('left',1.0),('right',1.0),('stop',1.0)])        #You can add your own command here
        print(v_command)
    except sr.UnknownValueError:
        print("say again")
    except sr.RequestError as e:
        print(e)
        pass
    
    if 'forward' in v_command:
        print(v_command)

    elif 'backward' in v_command:
        print(v_command)

    elif 'left' in v_command:
        print(v_command)

    elif "right" in v_command:
        print(v_command)

    elif 'stop' in v_command:
        print(v_command)

    else:
        pass
