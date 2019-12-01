import os
import random
import argparse
import subprocess
import webbrowser


def play_music():
    # TODO: YouTube streaming option
    music_dir_path = '/media/shan/Entertainment/Music/Anime/Naruto Music/'
    music_file = random.choice([
        f for f in os.listdir(music_dir_path)
        if f.endswith('.mp3')
    ])
    subprocess.run(['vlc', os.path.join(music_dir_path, music_file)])


def search(cmd):
    search_query = '+'.join(cmd.split()[1:])
    webbrowser.open('http://www.google.com/search?q=%s' % search_query)


def open_url(cmd):
    # TODO: Display error for invalid URLs
    url = cmd.split()[1]
    if not url.startswith('http://'):
        url = 'http://' + url
    webbrowser.open(url)


def main(cmd):
    print('Command:', cmd)
    
    if cmd == 'play music':
        play_music()
    elif cmd.startswith('search '):
        search(cmd)
    elif cmd.startswith('open '):
        open_url(cmd)
    else:
        print('Please enter a valid command.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cmd', help='Instructions for the assistant')
    args = parser.parse_args()

    main(args.cmd.lower().strip())
