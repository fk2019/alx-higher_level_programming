#!/usr/bin/python3
"""Module defines MyList class
"""


class MyList(list):
    """This class contains public instance method print_sorted()"""
    def __init__(self):
        """Initialize the classs"""
        super().__init__()

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
