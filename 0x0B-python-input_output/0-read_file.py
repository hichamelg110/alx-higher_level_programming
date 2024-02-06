#!/usr/bin/python3
"""File-reading utility function."""


def read_file(filename=""):
    """Reads and prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
