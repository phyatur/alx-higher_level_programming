#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ empty Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes empty Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ finds size """
        return self.width

    @size.setter
    def size(self, value):
        """ validates size """
        self.width = value
        self.height = value

    def __str__(self):
        """ prints the string representation """
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ assigns attributes to square """
        if len(args) != 0:
            i = 0
            square_attrs = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, square_attrs[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation """
        square_dict = {}
        square_attrs = ["id", "size", "x", "y"]
        for attr in square_attrs:
            square_dict[attr] = getattr(self, attr)
        return square_dict
