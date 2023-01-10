#!/usr/bin/python3
"""This module defines a say_my_name function
Args:
    first_name: The first name
    last_name: The last name(optional)

Raises:
    TypeError: first_name must be a string
    TypeError: last_name must be a string
"""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first_name> <last_name>"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
