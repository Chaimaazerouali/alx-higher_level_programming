#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry (7-base_geometry.py).

Instantiates with width and height, both of which must be private and positive integers,
validated by the integer_validator method from the base class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle with validated width and height."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

