import os
import random
import subprocess
import webbrowser

from bot import play_response


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
