#!/usr/bin/python3
""" find min number of a list """


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lw = 0
    hgt = len(list_of_integers)
    moy = ((hgt - lw) // 2) + lw
    moy = int(moy)
    if hgt == 1:
        return list_of_integers[0]
    if hgt == 2:
        return max(list_of_integers)
    if list_of_integers[moy] >= list_of_integers[moy - 1] and\
            list_of_integers[moy] >= list_of_integers[moy + 1]:
        return list_of_integers[moy]
    if moy > 0 and list_of_integers[moy] < list_of_integers[moy + 1]:
        return find_peak(list_of_integers[moy:])
    if moy > 0 and list_of_integers[moy] < list_of_integers[moy - 1]:
        return find_peak(list_of_integers[:moy])
