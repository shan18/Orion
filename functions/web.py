import webbrowser

from .utils import uri_exists, extract_query
from bot import play_response


def search(action_word, input_sentence):
    search_query = '+'.join(extract_query(action_word, input_sentence).split())
    play_response('Displaying results for %s from the web' % search_query)
    webbrowser.open('http://www.google.com/search?q=%s' % search_query)


def open_url(action_word, input_sentence):
    url = extract_query(action_word, input_sentence)
    if not url.startswith('https://'):
        url = 'https://' + url
    if not '.com' in url:
        # checked for '.com' as substring because url could be
        # of the form abc.com/xyz
        url += '.com'
    
    # URL validation
    if uri_exists(url):
        play_response('Opening %s' % url.split('://')[1])
        webbrowser.open(url)
    else:
        play_response('URL %s is invalid. Please try again.' % url.split('://')[1])
