#!/usr/bin/python3
"""1-rectangle class
"""


class Rectangle:
    """Define a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """config heigth
    """
    @property
    def height(self):
        return self.__height

    """Setter Height
    """
    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        elif type(value) != int:
            raise NameError("height must be an integer")
        elif value < 0:
            raise NameError("height must be >= 0")
    """Get the width
    """
    @property
    def width(self):
        return self.__width

    """config width
    """
    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        elif type(value) != int:
            raise NameError("width must be an integer")
        elif value < 0:
            raise NameError("width must be >= 0")
