#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square.

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

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of the current square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the current square is greater than or equal to the other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if the area of the current square is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the current square is less than or equal to the other."""
        return self.area() <= other.area()

