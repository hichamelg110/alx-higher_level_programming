#!/usr/bin/python3
"""File-appending utility function."""


def append_write(filename="", text=""):
    """Appends the provided text to a UTF8 text file with the given filename."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
