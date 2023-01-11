#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        m = 0
        s = 0
        for x in my_list:
            m += x[0] * x[1]
        for x in my_list:
            s += x[1]
        return m/s
