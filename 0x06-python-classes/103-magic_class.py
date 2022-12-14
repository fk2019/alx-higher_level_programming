#!/usr/bin/python3
"""This module defines a MagicClass class"""

import math


class MagicClass():
    """This class defines a MagicClass"""
    def __init__(self, radius=0):
        """Initialize class
        Args:
            radius: First parameter

        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns circumference"""
        return 2 * math.pi * self.__radius
