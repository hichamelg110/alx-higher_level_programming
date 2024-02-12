#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv
import os


class Base:
    '''the foundation for our object-oriented hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Converts a dictionary into a JSON string.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Converts a JSON string back into a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)
        
    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes an object's representation to a CSV file.'''
        if list_objs is None:
            list_objs = []

        f_name = "{}.json".format(cls.__name__)
        js_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(f_name, 'w') as file:
            file.write(js_string)
            
    @classmethod
    def load_from_file(cls):
        '''Reads a string from a file and converts it from JSON format.'''
        f_name = cls.__name__ + '.json'
        try:
            with open(f_name, 'r') as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj) for obj in list_dicts]
        except FileNotFoundError:
            return []
    @classmethod
    def save_to_file_csv(cls, objs):
        '''JSON string representation of an object to a file.'''
        csv_filename = cls.__name__ + '.csv'
        with open(csv_filename, 'w', newline='') as csv_file:
            if objs is not None and len(objs) > 0:
                csv_writer = csv.DictWriter(csv_file, fieldnames=objs[0].to_dictionary().keys())
                csv_writer.writeheader()
                for instance in objs:
                    csv_writer.writerow(instance.to_dictionary())
       
    @classmethod
    def load_from_file_csv(cls):
        '''Reads an object's representation from a CSV file.'''
        f_name = cls.__name__ + '.csv'
        if not os.path.exists(f_name):
            return []
        with open(f_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            list_dicts = [dict(row) for row in reader]
        return [cls.create(**dict) for dict in list_dicts]
