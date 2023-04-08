#!/usr/bin/python3
"""Make GET request using request module
"""
import requests


def req():
    """Use requests module to make request and return customized body
       response
    """
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url, auth=('user', 'pass'))
    body = req.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    req()
