#!/usr/bin/python3
"""
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Call the super class with id, x, y, width and height - this super
    call will use the logic of the __init__ of the Rectangle class.
    The width and height must be assigned to the value of size
    You must not create new attributes for this class, use all attributes
    of Rectangle - As reminder: a Square is a Rectangle with the same
    width and height
    All width, height, x and y validation must inherit from Rectangle
    - same behavior in case of wrong data
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        self.size = size
        super().__init__(size, size, x, y, id)


def __str__(self):
        """
        """
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)
        return s

@property
    def size(self):
        """
        size
        """
        return self.__width
