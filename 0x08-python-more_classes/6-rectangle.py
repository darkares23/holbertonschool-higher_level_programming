#!/usr/bin/python3
class Rectangle():

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            Perimeter = 0
        else:
            Perimeter = self.__height * 2 + self.__width * 2
        return Perimeter

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        return '\n'.join('#' * self.__width for _ in range(self.__height))

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
