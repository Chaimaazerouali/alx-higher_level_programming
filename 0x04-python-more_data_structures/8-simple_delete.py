#!/usr/bin/python3
def simple_delete(my_dir, key=""):
    if key in my_dir:
        del my_dir[key]
    return my_dir
