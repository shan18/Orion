import argparse


def main(cmd):
    print(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cmd', help='Instructions for the assistant')
    args = parser.parse_args()

    main(args.cmd)

