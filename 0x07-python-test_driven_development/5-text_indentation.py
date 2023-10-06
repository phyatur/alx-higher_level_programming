#!/usr/bin/python3
"""
A text indentation module
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    space = 0
    for char in text:
        if space == 0:
            if char == " ":
                continue
            else:
                print(char, end="")
                space = 1
        else:
            if char == "?" or char == "." or char == ":":
                print(char)
                print("")
                space = 0
            else:
                print(char, end="")
