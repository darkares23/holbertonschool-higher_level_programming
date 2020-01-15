#!/usr/bin/python3
"""Rectangule module
"""


class Rectangle:
    """Define a Rectangle class
    """
    def __init__(self, width=0, height=0):
        """init private intance atributes
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get method width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")@property
        self.__width = value

    @property
    def height(self):
        """Get method width """
        return self.__width

    @height.setter
    def height(self, value):
        """Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
