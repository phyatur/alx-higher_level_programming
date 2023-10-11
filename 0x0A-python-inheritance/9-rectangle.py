#!/usr/bin/python3
""" A 9-rectangle module that contains a subclass Rectangle """

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

    def area(self):
        """ returns area """
        return self.__width * self.__height

    def __str__(self):
        """returns official string representation """
        return f"[Rectangle] {self.__width}/{self.__height}"
