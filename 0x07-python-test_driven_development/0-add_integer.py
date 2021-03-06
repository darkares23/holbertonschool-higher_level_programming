#!/usr/bin/python3
"""
Sum module
cast float to int
Return the sum
"""


def add_integer(a, b=98):
    """
    This function returns the sum of two int
    """
    if (a is None):
        raise TypeError("a must be an integer")
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")
    return int(a + b)
