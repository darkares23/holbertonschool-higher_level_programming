#!/usr/bin/python3
"""
Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x,
                                               self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        if args:
            att_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dic_string = {'id': self.id, 'size': self.width,
                      'x': self.x, 'y': self.y}
        return dic_string

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
