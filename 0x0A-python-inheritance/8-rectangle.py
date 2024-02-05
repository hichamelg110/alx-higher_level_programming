#!/usr/bin/python3
'''Module for Rectangle class.'''


class BaseGeometry:
    '''Defines a BaseGeometry class.'''

    def area(self):
        '''Raises an Exception with a message".'''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    '''a Rectangle class that inherits from BaseGeometry.'''
    def __init__(self, width, height):
        '''The constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
