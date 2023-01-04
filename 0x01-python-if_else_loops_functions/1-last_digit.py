#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n > 0:
    i = n % 10
elif n < 0:
     i = (n % 10) * -1
else:
    i = 0
if (i > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(n, i))
elif (i < 6 & i != 0):
    print("Last digit of {:d} is {:d} and is less than 6 not 0".format(n, i))
else:
    print("Last digit of {:d} is {:d} and is 0".format(n, i))
