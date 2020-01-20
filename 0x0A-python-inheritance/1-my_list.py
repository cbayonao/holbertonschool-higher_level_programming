#!/usr/bin/python3
"""
Write a class MyList that inherits from list
Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
All the elements of the list will be of type int
"""


class MyList(list):
    def print_sorted(self):
        nl = self[:]
        nl.sort()
        print('{}'.format(nl))
