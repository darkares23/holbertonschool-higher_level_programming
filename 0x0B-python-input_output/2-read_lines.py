#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    num_lines = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines >= 0:
            print(f.read())
        for lines in f:
            if num_lines < nb_lines:
                print(lines, end="")
                num_lines += 1
