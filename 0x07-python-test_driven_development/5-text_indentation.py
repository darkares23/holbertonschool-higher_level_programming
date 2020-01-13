#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after these characters: ., ? and :
"""


def text_indentation(text):
    """
    print text funct
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = ""
    delim = {".", "?", ":"}
    i = 0
    for i in range(len(text)):
        if text[i] in delim:
            new_text += text[i]
            new_text = new_text.strip()
            print(new_text, end='')
            print("\n")
            new_text = ""
            i += 1
        else:
            new_text += text[i]
            i += 1
    if new_text != "":
        print(new_text.strip(), end='')
