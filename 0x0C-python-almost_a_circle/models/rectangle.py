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

        self.checker(height, "height")
        self.checker(widht, "width")
        self.checker(height, "x")
        self.checker(height, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def checker(self, value, param_name):
        """
        hp
        """
        if type(value is not int:
            raise TypeError(param_name + "must be an integer")
        if value <= 0 and param_name in ("width", "height"):
            raise ValueError(param + "must be > 0")
        if value < 0 and param_name in ("x", "y"):
            raise ValueError(param_name + "must be >= 0")

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__c = value

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
        if type(value) is not int:
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

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
