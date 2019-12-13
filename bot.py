import os
import nltk
import speech_recognition as sr
from gtts import gTTS
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


VOICE = True

INTENTS = (
    'MUS',
    'WEB',
    'SER'
)

FUNCTION_INTENT_MAP = {
    'music': 'MUS',
    'song': 'MUS',
    'open': 'WEB',
    'search': 'SER',
    'sleep': 'OFF',
    'exit': 'OFF',
    'abort': 'OFF',
    'quit': 'OFF'
}


def disable_voice():
    global VOICE
    VOICE = False


def extract_intent(sentence):
    lemm = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    clean_words = []
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        lemm_token = lemm.lemmatize(token)
        if not (lemm_token in stop_words or lemm_token == 'please'):
            clean_words.append(lemm_token)
        
    pos_tokens = nltk.pos_tag(clean_words)
    clean_words = []
    for pos_token in pos_tokens:
        if pos_token[1] in ['VB', 'NN', 'JJ', 'CD']:
            clean_words.append(pos_token[0])
    
    for word in clean_words:
        if word in FUNCTION_INTENT_MAP:
            return FUNCTION_INTENT_MAP[word], word
    return None, None


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
        instruction = input()
    print('You:', instruction)
    intent, action_word = extract_intent(instruction)
    if intent:
        return {
            'intent': intent,
            'action_word': action_word,
            'input': instruction.lower().strip()
        }
    return None


def play_response(text):
    if VOICE:
        audio_obj = gTTS(text=text, lang='en', slow=False)
        audio_obj.save('orion_response.mp3')
        os.system('mpg321 orion_response.mp3')
        os.remove('orion_response.mp3')
    else:
        print('Orion:', text)
