#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    if n >= 0:
        newStr += str[:n]
        newStr += str[n+1:]
    else:
        new_str = str
    return(new_str)
