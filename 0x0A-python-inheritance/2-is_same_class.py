#!/usr/bin/python3
"""
Module for checking the type of an object in Python.

This module contains a function `is_same_class` that checks
if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if `obj` is exactly an instance of `a_class`, False otherwise.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
