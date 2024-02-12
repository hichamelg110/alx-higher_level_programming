#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Foundation class for geometric rectangles.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor for the Rectangle class.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter method for width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width.'''
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method for height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height.'''
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter method for x-coordinate.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for x-coordinate.'''
        if not isinstance(value, int):
            raise TypeError("X-coordinate must be an integer")
        if value < 0:
            raise ValueError("X-coordinate must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter method for y-coordinate.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for y-coordinate.'''
        if not isinstance(value, int):
            raise TypeError("Y-coordinate must be an integer")
        if value < 0:
            raise ValueError("Y-coordinate must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
