#!/usr/bin/python3
def print_last_digit(number):
    if num < 0:
        i = (num * -1) % 10
    else:
        i = num % 10
    print("{}".format(i), end='')
    return i
