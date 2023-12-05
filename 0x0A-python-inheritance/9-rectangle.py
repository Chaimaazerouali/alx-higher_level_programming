#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry (7-base_geometry.py).
( Task based on 8-rectangle.py)

Instantiates with width and height, both of which must be private and positive integers,
validated by the integer_validator method from the base class.
Implements the area() method.
print() and str() methods provide the rectangle description: [Rectangle] <width>/<height>.
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

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description: [Rectangle] <width>/<height>."""
        return "[{}] {}/{}".format(__class__.__name__, self.__width, self.__height)

