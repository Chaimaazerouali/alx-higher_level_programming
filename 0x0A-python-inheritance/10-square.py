#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.

Square has an __init__ method for instantiation with a private 'size' attribute,
validated by the integer_validator from the base class. It implements the area() method.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""
    
    def __init__(self, size):
        """Initializes a Square instance with a validated size."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

