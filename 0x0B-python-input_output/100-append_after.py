#!/usr/bin/python3
"""
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as f:
        txt = f.readlines()
        line = []
        for i in range(len(txt)):
            line.append(txt[i])
            if search_string in txt[i]:
                line += new_string
        f.seek(0)
        f.write("".join(line))
