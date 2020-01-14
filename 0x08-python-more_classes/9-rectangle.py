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
        """Defines area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """Defines perimeter """
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
        str(column)
        return rectangle_string

    def __repr__(self):
        """return string representation"""
        return ("Rectangle({}, {})".format(self.width, self.__height))

    def __del__(self):
        """ Prints bye when del is exec"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
