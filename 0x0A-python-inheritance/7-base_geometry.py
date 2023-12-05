#!/usr/bin/python3
"""
Defines a BaseGeometry class with public methods area() and integer_validator().

- area(): Raises an exception indicating the method is not implemented.
- integer_validator(name, value): Validates that value is an integer.
  - Raises a TypeError if value is not an integer.
  - Raises a ValueError if value is less than or equal to 0.
"""

class BaseGeometry:
    """Empty BaseGeometry class."""

    def area(self):
        """Raises an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

