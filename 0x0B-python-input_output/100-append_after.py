#!/usr/bin/python3
"""Module inserts line of text toa text file, after each line containing
a specified string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string after line containing search_string"""
    text = ""
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
