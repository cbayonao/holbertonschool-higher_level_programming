#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = []
    for a in range(len(my_list)):
        if my_list[a] != search:
            cpy.append(my_list[a])
        else:
            cpy.append(replace)
    return cpy
