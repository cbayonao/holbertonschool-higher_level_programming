#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
    In the file models/rectangle.py
    Class Rectangle inherits from Base
    Private instance attributes, each with
    its own public getter and setter:
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)