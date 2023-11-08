#!/usr/bin/python3

def best_score(a_dictionary):
    k = None
    bt = -1
    if (a_dictionary is None):
        return k
    for c, d in a_dictionary.items():
        if d > bt:
            bt = d
            k = c
    return k
