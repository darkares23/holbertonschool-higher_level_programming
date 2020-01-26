#!/usr/bin/python3
"""
Base class file
"""
import json


class Base():
    """base representation class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """json string to a file """
        if list_objs is None:
            j_st = "[]"
        else:
            """used rectangle method to dicc to add new dicts to file"""
            j_st = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as fp:
            fp.write(j_st)

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
