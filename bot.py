import os
import speech_recognition as sr
from gtts import gTTS


VOICE = True


def disable_voice():
    global VOICE
    VOICE = False


def fetch_input():
    print('\nPlease enter an instruction:')
    if VOICE:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        instruction = recognizer.recognize_google(audio)
    else:
        instruction = input().lower().strip()
    instruction = instruction.lower().strip()
    print('You:', instruction)
    return instruction


def play_response(text):
    if VOICE:
        audio_obj = gTTS(text=text, lang='en', slow=False)
        audio_obj.save('orion_response.mp3')
        os.system('mpg321 orion_response.mp3')
        os.remove('orion_response.mp3')
    else:
        print('Orion:', text)
