#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
    my_list (list): The list of all elements.
    x (int): the number of elements of list to print.

    Return:
    The number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            print()
            return (count)
    print()
    return (count)
