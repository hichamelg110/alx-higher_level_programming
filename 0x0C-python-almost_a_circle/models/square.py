#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class for square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor for the Rectangle class.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of the square..'''
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter method for size.'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter method for size.'''
        self.width = value
        self.height = value

    def _upd_attributes(self, id=None, size=None, x=None, y=None):
    '''Updates the square's attributes.'''
    if id is not None:
        self.id = id
    if size is not None:
        self.size = size
    if x is not None:
        self.x = x
    if y is not None:
        self.y = y

    def update(self, *args, **kwargs):
    '''Updates the square's attributes using args or kwargs.'''
    if args:
        self._update_attributes(*args)
    elif kwargs:
        self._update_attributes(**kwargs)

    def to_dictionary(self):
    """Returns a dictionary representation of a Square."""    
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
