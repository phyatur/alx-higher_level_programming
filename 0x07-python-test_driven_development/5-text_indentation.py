#!/usr/bin/python3

"""
Module 5-text_indentation.py
Contains one function, text_indentation(text)
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each of these characters: ., ? and :


    Args:
        text: a text string


    Returns:
        a formatted tex output
    """
    
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    space_check = 0

    for char in text:
        if space_check == 0:
            if char == " ":
                continue
            else:
                print(char, end="")
                space_check = 1
        else:
            if char == "?" or char == "." or char == ":":
                print(char)
                print("")
                space_check = 0
            else:
                print(char, end="")
