#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = set(my_list)
    res = 0
    for a in n_list:
        res += a
    return res
