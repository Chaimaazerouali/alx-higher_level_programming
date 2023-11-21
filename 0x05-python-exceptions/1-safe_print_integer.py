#!/usr/bin/python3
import sys
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
    value (int): The int to print.

    Returns:
    if value has been correctly printed - True
    Otherwise - False.
    """
    rt = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        rt = False
    return rt
