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
        Size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Set size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
            """
            Adding the public method
            def update(self, *args, **kwargs) that assigns attributes:
            """
            if args:
                for i in range(len(args)):
                    if i == 0:
                        self.id = args[0]
                    if i == 1:
                        self.size = args[1]
                    if i == 2:
                        self.x = args[2]
                    if i == 3:
                        self.y = args[3]
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Adding the public method def to_dictionary(self):
        that returns the dictionary representation of a Square
        """
        mydict = {}
        attri = ['id', 'size', 'x', 'y']
        for key in attri:
            mydict.update({key: getattr(self, key)})
        return mydict
