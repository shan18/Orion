import os
import sys
import random
import argparse
import subprocess
import webbrowser
from gtts import gTTS
import speech_recognition as sr


def fetch_input(mode):
    print('\nPlease enter an instruction:')
    if mode == 'text':
        instruction = input().lower().strip()
    elif mode == 'voice':
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        instruction = recognizer.recognize_google(audio)
    instruction = instruction.lower().strip()
    print('You said:', instruction)
    return instruction


def play_response(text):
    audio_obj = gTTS(text=text, lang='en', slow=False)
    audio_obj.save('orion_response.mp3')
    os.system('mpg321 orion_response.mp3')
    os.remove('orion_response.mp3')


def play_music(music_dir_path, mode):
    if mode == 'local':
        play_response('Playing music from your computer')
        music_file = random.choice([
            f for f in os.listdir(music_dir_path)
            if f.endswith('.mp3')
        ])
        subprocess.run(['vlc', os.path.join(music_dir_path, music_file)])
    elif mode == 'online':
        play_response('Playing music from youtube')
        webbrowser.open('https://www.youtube.com/watch?v=LEh9F67Z5n8&list=PL3oW2tjiIxvQ60uIjLdo7vrUe4ukSpbKl')


def search(instruction):
    search_query = '+'.join(instruction.split()[1:])
    play_response('Displaying results for %s from the web' % search_query)
    webbrowser.open('http://www.google.com/search?q=%s' % search_query)


def open_url(instruction):
    # TODO: Display error for invalid URLs
    url = instruction.split()[1]
    play_response('Opening %s' % url)
    if not url.startswith('http://'):
        url = 'http://' + url
    webbrowser.open(url)


def main(args):
    while True:
        instruction = fetch_input(args.input_mode)
        if instruction == 'play music':
            play_music(args.music_dir, args.music_mode)
        elif instruction.startswith('search '):
            search(instruction)
        elif instruction.startswith('open '):
            open_url(instruction)
        elif instruction in ['exit', 'quit', 'close']:
            play_response('Logging out. Goodbye.')
            print('\nBye.')
            sys.exit(0)
        else:
            print('This is not a valid instruction.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_mode', default='voice', choices=['text', 'voice'],
        help='Mode of giving instructions to the assistant'
    )
    parser.add_argument(
        '--music_mode', default='online', choices=['local', 'online'],
        help='Play music locally or from youtube'
    )
    parser.add_argument(
        '--music_dir', default='/media/shan/Entertainment/Music/Anime/Naruto Music/',
        help='Directory containing files for playing music. This option is useless if music_mode is online'
    )
    args = parser.parse_args()

    main(args)
