#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
    value (int): The int to print.

    Returns:
    if value has been correctly printed - True
    Otherwise - False.
    """
    rst = False
    try:
        print("{:d}".format(value))
        rst = True
    except:
        rst = False
    return (rst)
