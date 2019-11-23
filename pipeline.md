# Project Pipeline


## Supported Functions

### Music

Orion will open vlc media player and play the songs present in a directory. Accepted commands for this intent:
  - play [some] music
  - play [a, some] song[s]
 
### Search

Orion will open up the web browser and search the given query. Accepted commands for this intent:
  - Search "query/keyword"
  - Lookup "query/keyword"

### Website

Orion the will open the requested website in the web browser. Accepted commands
 for this intent:
  - Open "website name"


## Intent Identification

Possible techniques:
  - Using training corpora and generating scores for each intent class
  - Use NLTK to find synonyms for action words (apply porter stemmer) in the input and match them with the given intent classes
  - Use POS Tag chunking regex sequence to find the correct intent


## Action Performance

Performing the action based on the identified intent


## Code Optimization

Optimize the overall algorithm.


## Voice Integration

Add voice based instructions.


## Wakeword Detection

This will ensure Orion stays active in background at all times.

