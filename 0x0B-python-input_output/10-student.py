#!/usr/bin/python3
"""Student class definition with selective attribute retrieval."""

class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with first name,
        last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            return {attr: getattr(self, attr) for attr in vars(self)}
        else:
            return {attr: getattr(self, attr) for attr in attrs if attr in vars(self)}
