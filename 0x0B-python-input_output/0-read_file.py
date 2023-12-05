#!/usr/bin/python3
""" 
Function that reads a text file (UTF-8) and prints its content to stdout.

Prototype: def read_file(filename=""):
Uses the with statement to ensure proper file handling.
Does not manage file permissions or handle file existence exceptions.

"""


def read_file(filename=""):
    """ read a file """
    if filename:
        with open(filename, mode="r", encoding='utf-8') as file:
            for line in file:
                print(line, end="")
