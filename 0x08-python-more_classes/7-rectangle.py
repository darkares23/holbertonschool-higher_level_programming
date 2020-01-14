#!/usr/bin/python3
"""Rectangule module
"""


class Rectangle:
    """Define a Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init private intance atributes
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get method width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")@property
        else:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """prints rectangle"""
        rectangle_string = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_string
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle_string += str(self.print_symbol)
            if row != self.__height:
                rectangle_string += "\n"
        rectangle_string = rectangle_string[:-1]
        str(column)
        return rectangle_string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
