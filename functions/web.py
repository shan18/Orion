import webbrowser

from .utils import uri_exists
from bot import play_response


def search(instruction):
    search_query = '+'.join(instruction.split()[1:])
    play_response('Displaying results for %s from the web' % search_query)
    webbrowser.open('http://www.google.com/search?q=%s' % search_query)


def open_url(instruction):
    url = ''.join(instruction.split()[1:])
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
