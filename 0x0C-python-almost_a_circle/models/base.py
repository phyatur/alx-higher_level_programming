#!/usr/bin/python3
"""
A base module

Contains a class Base
"""
import json
import csv


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the class """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb.objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string represntation of list_objs """
        new_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns instance with attributes already set """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instances """
        new_list = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        except:
            pass
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in csv format"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ is "Rectangle":
            attrs = ["width", "height", "x", "y", "id"]
        elif cls.__name__ is "Square":
            attrs = ["size", "x", "y", "id"]
        with open(filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=attrs)
            if list_objs is not None:
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in csv format """
        filename = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(filename, 'r', newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    new_list.append(row)
            return [cls.create(**obj) for obj in new_list]
        except FileNotFoundError:
            return [[]]
