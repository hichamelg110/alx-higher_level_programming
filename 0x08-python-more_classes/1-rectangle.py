#!/usr/bin/python3
"""This module defines a class Rectangle."""

class Rectangle:
    """This class models a geometric shape known as rectangle."""

    def __init__(self, width=0, height=0):
        """Constructs a new Rectangle instance.

        Args:
            width (int): The horizontal dimension of the new rectangle.
            height (int): The vertical dimension of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access or modify the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Adjusts the width of the Rectangle.

        Args:
            value (int): The desired width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Access or modify the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Adjusts the height of the Rectangle.

        Args:
            value (int): The desired height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

