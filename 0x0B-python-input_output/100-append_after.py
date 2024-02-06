#!/usr/bin/python3
"""File modification utility function."""

def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after a specific string in a text file.
    The new string is added after every occurrence of the search string in the file.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        for c, line in enumerate(lines):
            if search_string in line:
                lines[c] = line + new_string + '\n'
        file.seek(0)
        file.writelines(lines)
