#!/usr/bin/python3
"""
Defines a function is_same_class that returns True if the object is exactly an instance
of the specified class; otherwise, returns False.
"""

def is_same_class(obj, a_class):
    """Returns True if obj is an instance of the specified class; otherwise, False."""
    return type(obj) is a_class

