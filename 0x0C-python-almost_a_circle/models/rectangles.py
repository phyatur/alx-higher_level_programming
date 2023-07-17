#!/usr/bin/python3
""" First rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ method __init__ Initialization a Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ finds width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validates width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ finds height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validates height """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ finds x """
        return self.__x

    @x.setter
    def x(self, value):
        """ validates x """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ finds y """
        return self.__y

    @y.setter
    def y(self, value):
        """ validates y """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns area value of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character '#' """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ prints the string representation of the rectangle """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ updates the rectangle """
        if len(args) != 0:
            i = 0
            rect_attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, rect_attrs[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of rectangle """
        rect_dict = {}
        rect_attrs = ["id", "width", "height", "x", "y"]
        for attr in rect_attrs:
            rect_dict[attr] = getattr(self, attr)
        return rect_dict
