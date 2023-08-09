#!/usr/bin/python3

"""
Module 3-say_my_name.py
Contains one function,  say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>


    Args:
        first_name: a string
        last_name: a string


    Returns:
        a new string
    """
    
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
