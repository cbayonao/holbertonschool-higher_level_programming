#!/usr/bin/python3
"""3-rectangle class
"""


class Rectangle:
    """config rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Get the Width
    """
    @property
    def width(self):
        return self.__width

    """Config Width
    """
    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        elif type(value) != int:
            raise NameError("width must be an integer")
        elif value < 0:
            raise NameError("width must be >= 0")

    """Get the Heigth
    """
    @property
    def height(self):
        return self.__height

    """Config Height
    """
    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        elif type(value) != int:
            raise NameError("height must be an integer")
        elif value < 0:
            raise NameError("height must be >= 0")

    """get Area
    """
    def area(self):
        return self.__height*self.__width

    """get Perimeter
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * (self.__height + self.__width)
        return self.__perimeter

    """Print rectangle
    """
    def __str__(self):
        square = []
        if self.__width and self.__height:
            for i in range(0, self.__height):
                for j in range(self.__width):
                    square.append("#")
                if j <= self.__width:
                    square.append('\n')
            return "".join(square[:-1])
        else:
            square = ''
            return square

    """Print rectangle info
    """
    def __repr__(self):
        return "Rectangle" + "(" + str(self.__width)\
            + ", " + str(self.__height) + ")"

