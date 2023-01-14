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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of self"""
        d = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    for j in self.__dict__:
                        if i == j:
                            d[i] = self.__dict__[j]
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance"""
        for attr in self.__dict__:
            for key in json:
                if attr == key:
                    self.__dict__[attr] = json[key]
        return self.__dict__
