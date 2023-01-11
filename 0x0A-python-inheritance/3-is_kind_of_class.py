#!/usr/bin/python3
"""Module defines function that checks instance of a class object
"""


def is_kind_of_class(obj, a_class):
    """Returns True of obj is instance of a_class that may also inherit \
    from specified class"""
    if isinstance(obj, a_class):
        return True
    return False
