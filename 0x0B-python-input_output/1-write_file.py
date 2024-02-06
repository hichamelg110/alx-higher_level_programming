#!/usr/bin/python3
"""File-writing utility function."""


def write_file(filename="", text=""):
    """Writes the provided text to a UTF8 text file with the given filename."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
