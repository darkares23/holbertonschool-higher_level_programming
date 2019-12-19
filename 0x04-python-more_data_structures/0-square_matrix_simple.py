#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def pow2(x):
        return x ** 2
    i = 0
    new = matrix.copy()
    for row in matrix:
        new[i] = list(map(pow2, row))
        i+=1
    return new
