#!/usr/bin/python3
"""Send URL request and display value of `X-Request-Id` of the header
"""
import sys
import urllib.request
from urllib.error import URLError

try:
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.headers
        x_id = header["X-Request-Id"]
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    print(x_id)
