#!/usr/bin/python3
"""Rectangle class
"""


from models.base import Base
import json


class Rectangle(Base):
    """
    Rectangle class
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)

        self.checker(height, 'height')
        self.checker(width, 'width')
        self.checker(x, 'x')
        self.checker(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        get
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set
        """
        self.checker(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        get
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set
        """
        self.checker(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        get
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set
        """
        self.checker(value, 'x')
        self.__x = value

    @property
    def y(self):
        """
        get
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set
        """
        self.checker(value, 'y')
        self.__y = value

    def checker(self, value, param):
        """
        hp
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')
        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')
        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        get
        """
        return self.__height * self.__width

    def display(self):
        """
        set
        """
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        str Constructor
        """
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x,
                                                  self.y, self.width,
                                                  self.height)

        return string

    def update(self, *args, **kwargs):
        """
        Constructor
        """
        if args:
            argsList = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, argsList[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Constructor
        """
        dic_string = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x,
                      'y': self.y}
        return dic_string
