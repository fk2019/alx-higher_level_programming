#!/usr/bin/python3
"""Make POST request passing a parameter
"""
import requests
import sys


def post_email():
    """Use requests module to make request and return X-Request-Id
       value
    """
    url = sys.argv[1]
    data = sys.argv[2]
    payload = {'email': data}
    res = requests.get(url, params=payload)
    body = res.text
    print(f"Your email is: {body}")


if __name__ == "__main__":
    post_email()
