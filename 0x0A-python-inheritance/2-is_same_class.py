#!/usr/bin/python3
"""Module defines function is_same_class that checks instance of a class object
"""


def is_same_class(obj, a_class):
    """Returns True of obj is instance of a_class"""
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    return False
