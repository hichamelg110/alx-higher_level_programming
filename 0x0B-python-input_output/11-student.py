#!/usr/bin/python3
"""Student class definition with selective attribute retrieval and reloading from JSON."""

class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is not None:
            return {attr: getattr(self, attr) for attr in attrs if attr in vars(self)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Reloads the Student's attributes from a JSON object."""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

