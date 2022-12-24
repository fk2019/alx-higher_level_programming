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
        self.size = size

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size**2
