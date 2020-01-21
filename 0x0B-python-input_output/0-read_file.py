#!/usr/bin/python3
"""
Also can do it with lines.read(size)
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
