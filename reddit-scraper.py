from urllib2 import Request, url
from time import sleep
import json

_URL = 'http://www.reddit.com/'
_headers = {'User-agent': 'web:testapp (by /r/yourereallyfat)'}

# holds the URL in a Request object
request = Request(_URL, _headers)
# opens request object w urlopen
response = urlopen(request)
data = response.read()


def get_comments(URL,head,delay=2):
    '''Pretty generic call to urllib2.'''
    # suspends the current thread for (seconds)
    # ensure we don't GET too frequently or the API will block us
    sleep(delay) 
    request = Request(URL, headers=head)
    try:
        response = urlopen(request)
        data = response.read()
    except:
        sleep(delay+5)
        response = urlopen(request)
        data = response.read()
    return data

  