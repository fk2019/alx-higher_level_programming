#!/usr/bin/python3
"""Send POST request to provided URL
"""
import sys
from urllib import request
from urllib.error import HTTPError, URLError


def req():
    """Make POST req and send email address then return an utf-8
       body response
    """
    try:
        url = sys.argv[1]
        req = request.Request(url)
        with request.urlopen(req) as res:
            body = res.read()
            body = body.decode('utf-8')
    except HTTPError as e:
        print('Error code:', e.code)
    else:
        print(body)


if __name__ == "__main__":
    req()
