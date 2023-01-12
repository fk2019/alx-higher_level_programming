#!/usr/bin/python3
"""Module reads a text file and prints to stdout
"""


def read_file(filename=""):
    """Prints file contents to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
