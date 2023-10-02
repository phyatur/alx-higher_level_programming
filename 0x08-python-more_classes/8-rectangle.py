#!/usr/bin/python3

""" A Rectangle class that defines a rectangle """


class Rectangle:
    """ A rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle

        Args:
            width: Rectangle width
            height: Rectangle height

        """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        A meethod that returns the string version of rectangle
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        A method that returns official version of rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        A method that prints a message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A method that returns the biggest rectangle based on the area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
