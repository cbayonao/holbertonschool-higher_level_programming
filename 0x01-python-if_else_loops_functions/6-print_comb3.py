#!/usr/bin/python3
for a in range(0, 100):
    x = a / 10
    y = a % 10

    if x != y and x < y and a != 89:
        print("{}, ".format(a), end='')
    if a == 89:
        print("{}".format(a))
