import urllib.request


def read_webpage(url):
    response = urllib.request.urlopen(url)
    return response.read()