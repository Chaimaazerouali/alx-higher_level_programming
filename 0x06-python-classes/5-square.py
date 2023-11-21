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
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the length of a side of this square.

        Args:
            value (int): New length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Size must be an integer.')
        if value < 0:
            raise ValueError('Size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of this square.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints this square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j == self.size - 1 and i != j else "")
        print()

