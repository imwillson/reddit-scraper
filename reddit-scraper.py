from urllib2 import Request, urlopen
from time import sleep
import json

_URL = 'https://www.reddit.com/user/Yourereallyfat/comments'
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
    request = Request(URL, headers=head)

    # test print the dictionary
    # for key,value in head.iteritems():
    # 	print key,value



    try:
        response = urlopen(request)
        print("response was a sucess")
        data = response.read()
    except:
        sleep(delay+5)
        response = urlopen(request)
        data = response.read()

        print("error in function")
    return data




def main():

	try:	
		x = get_comments(_URL,_headers)
		print(x)
	except: 
		print("error")

if __name__ == "__main__":
	main()