#!/usr/bin/python3
"""This module defines an empty class Rectangle"""


class Rectangle():
    """This class defines a square"""
    def __init__(self, width=0, height=0):
        """Initialize class
        Args:
            width: First parameter
            height: Second parameter
        Raises:
            TypeError: width must be an integer, height must be an integer
            ValueError: width must be >= 0, height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for i in range(self.__height):
                str += "#" * self.__width
                str += "\n"
            str = str[:-1]
            return str

    def __repr__(self):
        w = str(self.__width)
        h = str(self.__height)
        res = "Rectangle(" + w + ", " + h +")"
        return res
