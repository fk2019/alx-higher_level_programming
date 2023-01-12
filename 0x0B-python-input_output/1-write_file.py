#!/usr/bin/python3
"""Module writes a string to a text file
"""


def write_file(filename="", text=""):
    """Write to file and return number of characters written"""
    with open(filename, mode="w", encoding='utf-8') as f:
        nb_chars = f.write(text)
    return nb_chars
