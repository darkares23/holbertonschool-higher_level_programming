#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sumAv = total = 0
    for x, y in my_list:
        sumAv += x * y
        total += y
    return sumAv / total
