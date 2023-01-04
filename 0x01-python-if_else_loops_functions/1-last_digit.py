#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lD = number % 10
elif number < 0:
    lD = (number % 10) * -1
else:
    lD = 0
if (lD > 5):
    print("Last digit of {:d} is {:d} and
 is greater than 5".format(number, lD))
elif (lD < 6 & lD != 0):
    print("Last digit of {:d} is {:d} and
 is less than 6 not 0".format(number, lD))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lD))
