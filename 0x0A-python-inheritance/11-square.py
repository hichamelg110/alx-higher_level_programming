#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A Square class that inherits from Rectangle.'''
    def __init__(self, size):
        '''The constructor.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Returns square's area.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns square's dimensions.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
