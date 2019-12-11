#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    x = chr(a)
    if a % 2 != 0:
        x = chr(a - 32)
    print("{}".format(x), end='')
