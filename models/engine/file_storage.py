#!/usr/bin/python3
"""A storage module to store data objects"""

import json
from models.base_model import BaseModel


class FileStorage:
    """File Storage Class

    Description:
    Stores object instances of various classes to a json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the objects of classes"""

        return self.__objects

    def new(self, obj):
        """Add New Objects

        Description:
        Sets new objects, obj into the dictionary of objects
        with the new object's class name and id in the format
        '<obj class name>.id'

        Args:
        obj (object): the new object to add to the dictionary
        of objects

        Returns:
        Nothing
        """

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """Serialize Objects

        Description:
        Serializes the dictionary of objects to the JSON file

        Returns:
        Nothing
        """

        objs = dict()
        for key, value in FileStorage.__objects.items():
            objs[key] = value.to_dict().copy()
        with open(self.__file_path, "w", encoding="UTF-8") as obj_file:
            json.dump(objs, obj_file)

    def reload(self):
        """Deserialize Objects

        Description:
        Deserializes the JSON file to a dictionary of objects only if
        the file exists. Otherwise, it does nothing.

        Returns:
        Nothing
        """

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as obj_file:
                objs = json.load(obj_file)

            for key, value in objs.items():
                obj_class_name = value.get("__class__")
                obj = eval(obj_class_name + "(**value)")
                self.__objects[key] = obj
        except FileNotFoundError:
            return
