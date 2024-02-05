#!/usr/bin/python3
'''Module for BaseGeometry class.'''

class BaseGeometry:
    '''Defines a BaseGeometry class.'''

    def area(self):
        '''Raises an Exception with the message "area() is not implemented".'''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
