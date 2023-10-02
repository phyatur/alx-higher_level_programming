#!/usr/bin/python3

""" A Rectangle class that defines a rectangle """


class Rectangle:
    """ A rectangle class """

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle

        Args:
            width: Rectangle width
            height: Rectangle height

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """  A method to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A method to set width attribute

        Args:
            value: new width

        Raises:
            TypeError: If the type of value is not an int
            ValueError: If value is less than or equal to 0

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  A method to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A method to set height attribute

        Args:
            value: new height

        Raises:
            TypeError: If the type of value is not an int
            ValueError: If value is less than or equal to 0

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        A method that returns the rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """
        A method that returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.height + 2 * self.width
