#!/usr/bin/python3
"""Send POST request to provided URL
"""
from urllib import request, parse
import sys


def post():
    """Make POST req and send email address then return an utf-8
       body response
    """
    url = sys.argv[1]
    email = sys.argv[2]
    email = email.encode('ascii')
    req = request.Request(url, email)
    with request.urlopen(req) as res:
        body = res.read()
        body = body.decode('utf-8')
    print(body)


if __name__ == "__main__":
    post()
