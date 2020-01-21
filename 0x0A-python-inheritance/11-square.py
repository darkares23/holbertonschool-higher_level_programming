#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        BaseGeometry.integer_validator(self, name="size", value=size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return(self.__size * self.__size)
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
