#!/usr/bin/python3
"""
Module for lookup methods
"""

def lookup(obj):
    """
    Returns a list of all attributes and methods of a given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings, each string being the name of an attribute or method of `obj`.
    """
    return dir(obj)
