#!/usr/bin/python3
"""Module defines Square class that inherits Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square that inherits Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
