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
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(j_st)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            retu = cls(1, 1)
        elif cls.__name__ == "Square":
            retu = cls(654)
        retu.update(**dictionary)
        return retu

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                pass
        except:
            return []
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
            instanceList = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in instanceList]

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            ret = json.loads(json_string)
            return ret
