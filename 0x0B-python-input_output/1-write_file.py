#!/usr/bin/python3
""" module 0-read_file that contains a function read_file """


def write_file(filename="", text=""):
    """ a function that returns the number of characters written """

    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
