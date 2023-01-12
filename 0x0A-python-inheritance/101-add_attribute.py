#!/usr/bin/python3
"""Module adds new attribute if possible to an object
"""


def add_attribute(obj, attr, value):
    """Returns object with new attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
