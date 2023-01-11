#!/usr/bin/python3
"""Module defines lookup function that returns available attributes and methods
"""


def lookup(obj):
    """Returns list of attraibutes and methods of an object"""
    return dir(obj)
