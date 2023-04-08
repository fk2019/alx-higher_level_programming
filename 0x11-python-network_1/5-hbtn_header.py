#!/usr/bin/python3
"""Make GET request using request and sys modules
"""
import requests
import sys


def header():
    """Use requests module to make request and return X-Request-Id
       value
    """
    url = sys.argv[1]
    req = requests.get(url, auth=('user', 'pass'))
    head = req.headers
    if (head['X-Request-Id']):
        x_req_id = head['X-Request-Id']
        print(x_req_id)


if __name__ == "__main__":
    header()
