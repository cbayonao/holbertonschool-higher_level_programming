#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods of an object
Returns a list object
Args: (obj) Object to lookup
"""


def lookup(obj):
    return dir(obj)
