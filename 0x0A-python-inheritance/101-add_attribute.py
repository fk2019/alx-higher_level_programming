#!/usr/bin/python3
"""Module adds new attribute if possible to an object
"""


def add_attribute(obj, attr, value):
    """Returns object with new attribute"""
    if type(obj) == type(attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
