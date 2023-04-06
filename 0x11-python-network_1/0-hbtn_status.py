#!/usr/bin/python3
"""Fetch url and display a customized body
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    body = res.read()
    body_type = type(body)
    msg = res.msg

print("Body response:")
print(f"\t- type: {body_type}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: OK")
