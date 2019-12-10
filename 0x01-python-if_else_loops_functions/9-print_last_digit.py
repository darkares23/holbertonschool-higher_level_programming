#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lastNumber = number % 10
    print("{}".format(lastNumber), end="")
    return(lastNumber)
