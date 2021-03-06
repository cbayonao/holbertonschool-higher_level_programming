#!/usr/bin/python3
"""
Class Base
"""
import json


class Base:
    """
    Class Base:
        Private class attribute __nb_objects = 0
        Class constructor: def __init__(self, id=None)
            if id is not None, assign the public instance
            attribute id with this argument value - you can
            assume id is an integer and you don’t need to
            test the type of it.
            otherwise, increment __nb_objects and assign the
            new value to the public instance attribute id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Adding the static method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Adding the class method that writes the JSON
        string representation of list_objs to a file
        """
        myjson = []
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string(myjson))
            else:
                for items in list_objs:
                    myjson.append(items.to_dictionary())
                myjson = cls.to_json_string(myjson)
                file.write(myjson)
