#!/usr/bin/python3
"""This script defines the Square class."""

class Square:
    """Represents a square.

    Attributes:
        __size (int): Length of a side of the square.
    """

    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int): Length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('Size must be an integer.')
        if size < 0:
            raise ValueError('Size must be >= 0.')
        self.__size = size

    def area(self):
        """Calculate the area of this square.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2

