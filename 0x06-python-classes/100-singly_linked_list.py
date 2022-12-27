#!/usr/bin/python3
"""This module defines a Node class and SinglyLinkedList class"""


class Node():
    """This class defines a node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns data"""
        return self.__data

    @property
    def next_node(self):
        """Returns next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """This class defines a singly linked list"""
    def __init__(self):
        """Initialize a class"""
        self.__head = None

    def __str__(self):
        res = []
        current = self.__head
        while current is not None:
            res.append(str(current.data))
            current = current.next_node
        return "\n".join(res)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the
        list (increasing order)
        Args:
            value: First parameter
        """
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None
                   and current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new
