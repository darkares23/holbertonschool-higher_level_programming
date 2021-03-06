#!/usr/bin/python3

""" Defines a node in a sinly linked list"""


class Node:
    def __init__(self, data, next_node=Node):
        """Initiates the instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node or value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__spot = value


class SinglyLinkedList:
    """
    Methods of the SinglyLinkedListClass
    """

    def __init__(self):
        self.__head = None

    def insert_node(self, value):
        """insert node in sorted order"""
        tmp = self.__head
        new = Node(value, self.__head)

        if tmp is None:
            self.__head = new
            return
        if tmp.data > value:
            new.next_node = tmp
            self.__head = new
            return
        
