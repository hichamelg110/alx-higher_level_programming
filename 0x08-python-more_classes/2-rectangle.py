#!/usr/bin/python3
"""This module introduces a class named Rectangle."""

class Rectangle:
    """This class models a geometric entity known as a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructs a new instance of Rectangle.

        Args:
            width (int): The horizontal span of the rectangle.
            height (int): The vertical span of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access or modify the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Access or modify the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
