#!/usr/bin/python3
"""
text identation module
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    delim = {".", "?", ":"}

    for char in text:
        if char in delim:
            print(char, end="")
            print("\n")
            flag = 1
        else:
            if flag == 0:
                print(char, end="")
            else:
                if char == " " or char == "\t":
                    pass
                else:
                    print(char, end="")
                    flag = 0
