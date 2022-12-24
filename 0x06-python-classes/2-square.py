#!/usr/bin/python3
"""This moduel defines a class Square"""


class Square():
    """This class defines a square"""
    def __init__(self, size=0):
        """Initialize class
        Args:
            size: First parameter

        Raises:
            TypeError: Size must be an int
            ValueError: Size must be >= 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
