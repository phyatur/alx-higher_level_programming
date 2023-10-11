#!/usr/bin/python3
""" module 1-number_of_lines.py that contains a function number_of_lines """


def write_file(filename="", text=""):
    """ a function that returns the number of characters written """
    with open(filename, mode="r", encoding="utf-8") as f:
        f.write(text)
    return len(text)
