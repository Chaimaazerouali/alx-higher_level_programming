#!/usr/bin/python3
"""
Defines a function is_kind_of_class that returns True if the object is
an instance of, or if the object is an instance of a class that inherited from,
the specified class; otherwise, returns False.
"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of the specified class or its subclasses; otherwise, False."""
    return isinstance(obj, a_class)

