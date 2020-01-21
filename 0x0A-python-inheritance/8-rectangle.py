#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry
Instantiation with width and height:
def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers,
validated by integer_validator
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator('height', height)
        self.integer_validator('width', width)
        self.__height = height
        self.__width = width

