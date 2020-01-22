#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    pascal = []
    if n > 1:
        for i in range(n):
            pascal.append(rows(i))
    return pascal


def rows(n):
    row = str(11 ** n)
    return [num for num in row]
