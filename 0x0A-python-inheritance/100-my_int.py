#!/usr/bin/python3
"""
Defines a MyInt class that inverts the behavior of '==' and '!=' for int objects.
"""

class MyInt(int):
    """Inverted equality for the int class."""

    def __eq__(self, other):
        """Overrides the '==' operator to return False when objects are of the same type."""
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        """Overrides the '!=' operator to return True when objects are of the same type."""
        if isinstance(self, type(other)):
            return True

