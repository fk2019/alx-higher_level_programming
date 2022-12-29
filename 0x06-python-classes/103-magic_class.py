#!/usr/bin/python3
import math
"""This module defines a MagicClass class"""


class MagicClass():
    """This class defines a MagicClass"""
    def __init__(self):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2*math.pi*self.__radius
