#!/usr/bin/python3
"""
Function that returns the number
of lines of a text file
"""


def number_of_lines(filename=""):
    cont = 0
    with open(filename) as f:
        for l in f.readlines():
            cont += 1
    return cont
