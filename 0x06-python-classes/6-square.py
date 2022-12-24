#!/usr/bin/python3
"""This moduel defines a class Square"""


class Square():
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize class
        Args:
            size: First parameter
            position: Second parameter

        Raises:
            TypeError: Size must be an int, Position must be a
        tuple of posiive integers
            ValueError: Size must be >= 0
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """Returns size"""
        return self.__size

    @property
    def position(self):
        """Returns position"""
        return self.__position
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        """Returns area of square"""
        return self.__size**2

    def my_print(self):
        """Prints square with # character to stdout"""
        if self.__size == 0:
            print()
        else:
            print("\n"*self.__position[1], end="")
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
