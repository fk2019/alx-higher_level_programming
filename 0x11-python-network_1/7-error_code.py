#!/usr/bin/python3
"""Make GET request and dislay error code
"""
import requests
import sys


def error_code():
    """Use requests module to make request and return error code
       if available
    """
    url = sys.argv[1]
    res = requests.get(url)
    code = res.status_code
    print(f"Error code: {code}")


if __name__ == "__main__":
    error_code()
