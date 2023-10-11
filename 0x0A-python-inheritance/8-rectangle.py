#!/usr/bin/python3
""" A 8-rectangle module thath contains a subclass Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines class Rectangle """

    def __init__(self, width, height):
        """ initializes Rectangle and
        validates width and height with integer_validator """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
