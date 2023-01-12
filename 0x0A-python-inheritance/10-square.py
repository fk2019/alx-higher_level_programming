#!/usr/bin/python3
"""Module defines Square class and inherits Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle class"""
    def __init__(self, size):
        """Initialize the class"""
        super().__init__(self.__size, self.__size)
        self.integer_validator("size", self.__size)
        self.__size = size

    def __str__(self):
        """Return string"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
