#!/usr/bin/python3
"""This module defines a print_square function
Args:
    size: size of square

Raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0
"""


def print_square(size):
    """Prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    for i in range(size):
        print("#" * size)
