#!/usr/bin/python3
"""Module returns dictionary description of an object
"""


def class_to_json(obj):
    """Returns dictionary description of an obj"""
    return obj.__dict__
