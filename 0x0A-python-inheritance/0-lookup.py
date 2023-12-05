#!/usr/bin/python3
"""
Returns a list of attributes and methods for a given object.
"""

def lookup(obj):
    """Returns a list of attributes and methods of the given object."""
    return [method for method in dir(obj)]

