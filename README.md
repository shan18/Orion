# Orion - An Intelligent Voice-Based Assistant

## Installing Requirements

1. Install packages for speech to text conversion  
`$ sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio`

2. Install package for playing orion's voice-based responses  
`$ sudo apt-get install mpg321`

3. Install other requirements  
`$ pip install -r requirements.txt`

4. Download the necessary NLTK packages  
`$ python -m nltk.downloader wordnet`  
`$ python -m nltk.downloader punkt`  
`$ python -m nltk.downloader stopwords`  
`$ python -m nltk.downloader averaged_perceptron_tagger`


## Using Orion

You can start interacting with Orion by running the script  
`$ python orion.py`  

If you don't want to interact via voice, there is also a text-based option  
`$ python orion.py --text_mode`  

To turn off Orion, you can use the action words: `sleep`, `quit`, `exit`


## Supported Functions

### Music

Orion can play music either online from YouTube or locally from a directory in you system containing audio files. If you want to play music locally, then make sure your system has vlc media player installed on it and also specify the flags `--music_mode` and `--music_dir` accordingly while running the script `orion.py`.  
Example commands: `play music`, `can you play some songs` e.t.c.

### Web

You can tell Orion to open any website via the action word `open`.  
Example commands: `open google`, `open twitter.com` e.t.c.

### Search

You can tell Orion to perform a google search on your browser via the action word `search`.  
Example command: `search ai with python`, `do a search intelligent voice-based virtual assistant`  

\* More Functionalities to be added soon

## Tested Platform

Linux x86 (Ubuntu 18.04) 64 bit with python 3.6.9
