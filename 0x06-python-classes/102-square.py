#!/usr/bin/python3
"""This module defines a Square class"""


class Square(object):
    """This class defines a square"""
    def __init__(self, size=0):
        """Initialize class
        Args:
            size: First parameter

        Raises:
            TypeError: Size must be a number
            ValueError: Size must be >= 0
        """
        self.size = size

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of a square"""
        return self.__size ** 2

    def __lt__(self, other):
        assert isinstance(other, Square)
        return self.size < other.size

    def __le__(self, other):
        assert isinstance(other, Square)
        return self.size <= other.size

    def __eq__(self, other):
        assert isinstance(other, Square)
        return self.size == other.size

    def __ne__(self, other):
        assert isinstance(other, Square)
        return self.size != other.size

    def __gt__(self, other):
        assert isinstance(other, Square)
        return self.size > other.size

    def __ge__(self, other):
        assert isinstance(other, Square)
        return self.size >= other.size
