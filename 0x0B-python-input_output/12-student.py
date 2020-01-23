#!/usr/bin/python3
"""
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = dict()
        if attrs:
            for i in range(0, len(attrs)):
                if attrs[i] in self.__dict__:
                    dic[attrs[i]] = self.__dict__[attrs[i]]
        if attrs is None:
            dic = self.__dict__
        return dic
