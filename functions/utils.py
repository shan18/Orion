import requests


def uri_exists(uri):
    try:
        with requests.get(uri, stream=True) as response:
            try:
                response.raise_for_status()
                return True
            except requests.exceptions.HTTPError:
                return False
    except requests.exceptions.ConnectionError:
        return False


def extract_query(action, sentence):
    return sentence[sentence.find(action) + len(action) + 1:]
