#!/usr/bin/python3
"""
 function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    size = len(list_of_integers)

    if size == 0:
        return None
    mid = size // 2
    midE = size

    while 1:
        midE = midE // 2
        if (list_of_integers[mid] < list_of_integers[mid + 1]):
            if midE // 2 == 0:
                midE = 2
        return
