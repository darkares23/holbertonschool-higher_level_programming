#!/usr7bin/python3
def number_of_lines(filename=""):
    num_lines = 0
    with open(filename, encoding="utf-8") as f:
        for l in f:
            num_lines += 1
        str(l)
        return num_lines