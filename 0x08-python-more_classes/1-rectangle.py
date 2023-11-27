#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes.
"""

class Rectangle:
    """ Defines a rectangle with width and height attributes """

    def __init__(self, width=0, height=0):
        """ Initializes height and width """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @property
    def width(self):
        """ Retrieves width """
        return self.__width

    @height.setter
    def height(self, value):
        """ Sets height with a new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ Sets width with a new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
