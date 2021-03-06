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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method def area(self): that returns
        the area value of the Rectangle
        """
        return self.__height*self.__width

    def display(self):
        """
        Public method def display(self): that prints
        in stdout the Rectangle instance with the
        character #
        """
        for y in range(0, self.__y):
            print()
        for a in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for b in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        __str__ method so that it returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] " + "(" + str(self.id) + ") "\
            + str(self.__x) + "/"\
            + str(self.__y) + " - " + str(self.__width) + "/"\
            + str(self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                if a == 1:
                    self.width = args[1]
                if a == 2:
                    self.height = args[2]
                if a == 3:
                    self.x = args[3]
                if a == 4:
                    self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Adding the public method that returns the
        dictionary representation of a Rectangle
        """
        def to_dictionary(self):
            """
        Dict Rep of Rectangle Class
        """
        mydict = {}
        attri = ['x', 'y', 'id', 'width', 'height']
        for key in attri:
            mydict.update({key: getattr(self, key)})
        return mydict
