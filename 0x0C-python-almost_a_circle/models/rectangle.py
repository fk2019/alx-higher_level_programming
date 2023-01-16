#!/usr/bin/python3
"""Moduel defines Rectangle class that inherits Base class
"""

from models.base import Base


class Rectangle(Base):
    """This class inherits from Base and defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            self.___width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    @property
    def x(self):
        """Return x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        """Return y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            self.__y = value