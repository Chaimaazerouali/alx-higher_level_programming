#!/usr/bin/python3
def safe_print_integer(value):
    rt = False
    try:
        print("{:d}".format(value))
        rt = True
    except:
        rt = False
    return (rt)
