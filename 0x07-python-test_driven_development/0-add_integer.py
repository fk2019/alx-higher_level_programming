#!/usr/bin/python3
"""This function adds two integers

Args:
    a: First parameter
    b: Second parameter

Raises
    TypeError: a must be an integer, b must be an integer
"""


def add_integer(a, b=98):
    """Returns sum of a and b"""
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(int(a)) is not int or type(int(b)) is not int:
        raise ValueError("cannot convert float NaN to integer")
    return (int(a) + int(b))
