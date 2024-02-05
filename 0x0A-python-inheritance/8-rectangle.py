#!/usr/bin/python3
'''Module for Rectangle class.'''

class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Raises an Exception with a message.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''A Rectangle class that inherits from BaseGeometry.'''
    def __init__(self, width, height):
        '''The constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
