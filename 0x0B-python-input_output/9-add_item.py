#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""


import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

fil3 = 'add_item.json'

mylist = []

if os.path.isfile(fil3):
    mylist = load_from_json_file(fil3)

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        mylist.append(i)
save_to_json_file(mylist, fil3)
