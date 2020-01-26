#!/usr/bin/python3
"""
Rectangle class file
"""
from models.base import Base
import json


class Rectangle(Base):
    """Rectangle representation class"""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__c = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print the rectangle using #"""
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x,
                                                  self.y, self.width,
                                                  self.height)

        return string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            argsList = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, argsList[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dic_string = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x,
                      'y': self.y}
        return dic_string
