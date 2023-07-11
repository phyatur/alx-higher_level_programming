#!/usr/bin/python3
""" Student class """


class Student:
    """ defines class Student """

    def __init__(self, first_name, last_name, age):
        """ initialize new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieve dictionary representation of a Student instance """
        return self.__dict___
