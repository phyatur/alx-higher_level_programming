#!/usr/bin/python3
""" A 7-base_geometry module that contains a class BaseGeometry """


class BaseGeometry():
    """ Defines class Geometry """

    def area(self):
        """ raises Exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(name) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
