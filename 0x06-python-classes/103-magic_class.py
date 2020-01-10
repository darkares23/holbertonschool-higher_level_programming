#!/usr/bin/python3
"""
  Circle Math
"""


class MagicClass:
    """ Magic Circle """
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Area Math """
        return ((self.__radius) ** 2) * math.pi

    def circumference(self):
        """ Circum Math """
        return 2 * math.pi * self.__radius
