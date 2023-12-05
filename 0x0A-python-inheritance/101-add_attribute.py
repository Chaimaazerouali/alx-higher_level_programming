#!/usr/bin/python3
"""
Defines a function add_attribute that adds a new attribute to an object when possible.
"""

def add_attribute(obj, attr, value):
    """Adds a new attribute to the object if possible."""
    setattr(obj, attr, value)

