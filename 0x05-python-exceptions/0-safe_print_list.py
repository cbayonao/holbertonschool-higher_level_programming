#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for n in range(x):
        try:
            print("{}".format(my_list[i]))
            i += 1
        except:
            pass
        print()
        return i
