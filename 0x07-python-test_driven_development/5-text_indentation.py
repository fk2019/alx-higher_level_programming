#!/usr/bin/python3
"""This module defines a text_indentation() function
Args:
    text: Text to evaluate

Raises:
    TypeError: text must be a string
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ".", "?", and ":"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if flag == 0:
            if c == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if c == "." or c == "?" or c == ":":
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
