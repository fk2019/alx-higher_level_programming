#!/usr/bin/python3
"""Module defines Square class that inherits Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square that inherits Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class"""
        super().__init__(size, size, x, y, id)
