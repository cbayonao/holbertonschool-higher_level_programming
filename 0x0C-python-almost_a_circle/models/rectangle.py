#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
    In the file models/rectangle.py
    Class Rectangle inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Private instance attributes, each with
    its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor:
        Call the super class with id - this super call with
        use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
