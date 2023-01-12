#!/usr/bin/python3
"""Module appends string to end of file
"""


def append_write(filename="", text=""):
    """Append string to end of file nd return number of characters written"""
    with open(filename, mode="a", encoding='utf-8') as f:
        nb_chars = f.write(text)
    return nb_chars
