#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
Create the file if doesn’t exist.
Overwrite the content of the file if it already exists.
"""


def write_file(filename="", text=""):
    with open(filename, 'w+') as f:
        return f.write(text)
