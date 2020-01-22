#!/usr/bin/python3
"""
Function that reads n lines of a text file (UTF8)
and prints it to stdout
Read the entire file if nb_lines is lower or equal
to 0 OR greater or equal to the total number of lines of the file
"""


def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            txt = f.read()
            print(txt, end='')
        else:
            for line in f:
                print(line, end='')
                i += 1
                if i == nb_lines:
                    break
