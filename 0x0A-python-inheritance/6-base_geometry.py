#!/usr/bin/python3
"""
Defines a BaseGeometry class with a public method area() that raises an exception
indicating the method is not implemented.
"""

class BaseGeometry:
    """Empty BaseGeometry class."""

    def area(self):
        """Raises an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

