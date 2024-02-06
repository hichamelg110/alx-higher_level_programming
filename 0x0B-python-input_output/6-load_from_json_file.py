#!/usr/bin/python3
"""JSON deserialization utility function."""
import json


def load_from_json_file(filename):
    """Loads a Python object from a text file in JSON format."""
    with open(filename) as file:
        return json.load(file)
