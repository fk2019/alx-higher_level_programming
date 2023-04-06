#!/usr/bin/python3
"""Fetch url and display a customized body
"""
import urllib.request
from urllib.error import URLError

try:
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        body_type = type(body)
        msg = res.msg
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    print("Body response:")
    print(f"\t- type: {body_type}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: OK")
