#!/usr/bin/python3
"""Module defines BaseGeometry class and Rectangle that inherits from it
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize class"""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """Return string"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                                    self.__height))
