#!/usr/bin/python3
"""
Square Module
"""
def print_square(size):
    """Print square func"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
