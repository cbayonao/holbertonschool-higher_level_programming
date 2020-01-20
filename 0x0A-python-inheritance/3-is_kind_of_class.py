#!/usr/bin/python3
"""
Function that verify if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
Return True if is the same, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
