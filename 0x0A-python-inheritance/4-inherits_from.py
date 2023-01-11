#!/usr/bin/python3
"""Module defines function that checks instance of a class object
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a_class that inhetited \
    from specified class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
