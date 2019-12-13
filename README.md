# Orion - An intelligent voice-based assistant

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
