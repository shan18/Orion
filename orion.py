import sys
import argparse

from bot import fetch_input, play_response, disable_voice
from functions.web import search, open_url
from functions.music import play_music


def main(args):
    while True:
        instruction = fetch_input()
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
        '--text_mode', action='store_true',
        help='Switch the assistant to text mode'
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

    if args.text_mode:
        disable_voice()

    main(args)
