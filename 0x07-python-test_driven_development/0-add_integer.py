#!/usr/bin/python3
"""This function adds two integers

Args:
    a: First parameter
    b: Second parameter

Raises
    TypeError: a must be an integer, b must be an integer
"""


def add_integer(a, b=98):
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
