#!/usr/bin/python3
"""Dsiplay id of my GitHub using the GitHub API
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def my_github():
    """Get my git gub id
    """
    api = 'https://api.github.com/user'
    user = sys.argv[1]
    pwd = sys.argv[2]
    basic = HTTPBasicAuth(user, pwd)
    req = requests.get(api, auth=basic)
    id = req.json().get("id")
    print(id)


if __name__ == "__main__":
    my_github()
