#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and hasattr(self, '__dict__'):
            new_dic = {}
            for at in attrs:
                if at in self.__dict__ and type(at) is str:
                    new_dic[at] = self.__dict__[at]
            return new_dic
        else:
            return self.__dict__.copy()
