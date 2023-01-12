#!/usr/bin/python3
"""Module defines MyInt class that inherits int
"""


class MyInt(int):
    """This class inverts == and != operaters"""
    def __init__(self, value=0):
        """Initialize class"""
        self.value = value
        super().__init__()

    def __eq__(self, value):
        return super().__eq__(self) + self is value

    def __ne__(self, value):
        return super().__ne__(self) + self == value
