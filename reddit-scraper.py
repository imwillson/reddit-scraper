from urllib2 import Request, urlopen
from time import sleep
import json

_URL = 'http://www.reddit.com/user/Youreallyfat/comments/.json'
_headers = {'User-Agent': 'reddit-scraper v1.0 (by /u/Yourereallyfat )'}

# # holds the URL in a Request object
# request = Request(_URL, _headers)
# # opens request object w urlopen
# response = urlopen(request)
# data = response.read()


def get_comments(URL,head,delay=2):
    # suspends the current thread for (seconds)
    # ensure we don't GET too frequently or the API will block us
    sleep(delay) 
    request = Request(URL, "", head)
    try:
        response = urlopen(request)
        data = response.read()
    except:
        sleep(delay+5)
        response = urlopen(request)
        data = response.read()
    return data




def main():
	try:	
		x = get_comments(_URL,_headers)
		print(x)
	except: 
		print("error")

if __name__ == "__main__":
	main()