#!/usr/bin/python3
'''Module for checking the type of an object.'''


def is_kind_of_class(obj, a_class):
    '''Checks if an object is an instance of a specified class or its subclasses.'''
    return isinstance(obj, a_class)
