#!/usr/bin/python3
'''Checks object inheritance.'''


def inherits_from(obj, a_class):
    '''Checks if object is a subclass instance.'''
    return isinstance(obj, a_class) and type(obj) != a_class
