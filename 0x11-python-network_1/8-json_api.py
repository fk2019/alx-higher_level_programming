#!/usr/bin/python3
"""Make POST request and dislay body
"""
import requests
import sys


def json_api():
    """Use requests module to make request and return
       response body
    """
    url = 'http://0.0.0.0:5000/search_user'
    param = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": param}
    res = requests.get(url, data=payload)
    try:
        json = res.json()
        if (json == {}):
            print("No result")
        else:
            print(f"[{json.get(id)}] {json.get(name)}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    json_api()
