#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        d = 0
        for t in my_list:
            num += (t[0] * t[1])
            d += t[1]
        return (num / d)
    return 0
