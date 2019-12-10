#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ultimo = number % 10
else:
    ultimo = number % -10
if ultimo == 0:
    print("Last digit of {0} is {1} and is 0".format(number, ultimo))
elif ultimo > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, ultimo))
elif ultimo < 6:
    print("Last digit of {0} is {1}\
    and is less than 6 and not 0".format(number, ultimo))
