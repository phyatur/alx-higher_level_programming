#!/usr/bin/python3
""" module 0-read_file that contains a function read_file """


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout: """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
