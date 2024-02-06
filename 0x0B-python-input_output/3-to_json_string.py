#!/usr/bin/python3
"""JSON serialization utility function."""

def to_json_string(my_obj):
    """returns the JSON representation of an object (string)."""
    json_use = json.dumps(my_obj)
    return json_use
