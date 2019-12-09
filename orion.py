import os
import sys
import random
import argparse
import subprocess
import webbrowser


def play_music(music_dir_path, mode):
    if mode == 'local':
        music_file = random.choice([
            f for f in os.listdir(music_dir_path)
            if f.endswith('.mp3')
        ])
        subprocess.run(['vlc', os.path.join(music_dir_path, music_file)])
    elif mode == 'online':
        webbrowser.open('https://www.youtube.com/watch?v=LEh9F67Z5n8&list=PL3oW2tjiIxvQ60uIjLdo7vrUe4ukSpbKl')


def search(instruction):
    search_query = '+'.join(instruction.split()[1:])
    webbrowser.open('http://www.google.com/search?q=%s' % search_query)


def open_url(instruction):
    # TODO: Display error for invalid URLs
    url = instruction.split()[1]
    if not url.startswith('http://'):
        url = 'http://' + url
    webbrowser.open(url)


def main(args):
    instruction = input('Please enter an instruction:\n').lower().strip()
    while True:
        if instruction == 'play music':
            play_music(args.music_dir, args.music_mode)
        elif instruction.startswith('search '):
            search(instruction)
        elif instruction.startswith('open '):
            open_url(instruction)
        elif instruction in ['exit', 'quit', 'close']:
            print('\nBye.')
            sys.exit(0)
        else:
            print('Please enter a valid instruction.')
        instruction = input('\nPlease enter the next instruction:\n').lower().strip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
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
