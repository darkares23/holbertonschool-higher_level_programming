#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        string = ""
        for line in f:
           if search_string in line:
               string += line + new_string
           else:
               string += line
        f.close()
    with open(filename, mode='w') as f:
        f.write(string)
