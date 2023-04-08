#!/usr/bin/python3
"""Send POST request to provided URL
"""
import sys
from urllib import request, parse
from urllib.error import URLError


def post():
    """Make POST req and send email address then return an utf-8
       body response
    """
    try:
        url = sys.argv[1]
        email = sys.argv[2]
        email = email.encode('ascii')
        req = request.Request(url, email)
        with request.urlopen(req) as res:
            body = res.read()
            body = body.decode('utf-8')
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        print(body)


if __name__ == "__main__":
    post()
