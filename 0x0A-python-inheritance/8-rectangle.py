#!/usr/bin/python3
"""Module defines BaseGeometry class and Rectangle that inherits from it
"""


class BaseGeometry(object):
    """This class raises an Exception"""
    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize class"""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
