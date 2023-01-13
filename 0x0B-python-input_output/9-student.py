#!/usr/bin/python3
"""Module defines Student class that defines a student
"""


class Student():
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of self"""
        return self.__dict__
