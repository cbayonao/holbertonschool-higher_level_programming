#!/usr/bin/python3
"""
Function that just reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    with open(filename) as f:
        print(f.read(), end='')
