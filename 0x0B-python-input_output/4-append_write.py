#!/usr/bin/python3
"""
Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
If the file doesn’t exist, it should be created
"""


def append_write(filename="", text=""):
    with open(filename, 'a+') as f:
        return f.write(text)
