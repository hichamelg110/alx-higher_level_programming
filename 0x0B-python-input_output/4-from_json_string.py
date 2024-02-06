#!/usr/bin/python3
"""JSON deserialization utility function."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    json_use = json.loads(my_str)
    return json_use
