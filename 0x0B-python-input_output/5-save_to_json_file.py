#!/usr/bin/python3
"""JSON serialization utility function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file in JSON format."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
