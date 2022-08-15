#!/usr/bin/python3
"""
Module file_storage.py
Handles serialization and deserialization
of instances to and from json
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Private class attributes
        __file_path: string
        __objects: dictionary
    Public instance methods
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    # Path to file where json will be stored
    __file_path = "file.json"
    # Stores all objects by <class name>.id
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj:
            # Create the key
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes serializes __objects to the JSON file """
        obj_dict = {}

        # Iterate through __objects
        # Convert each object to a dictionary
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        # Open file , serialize, and write to file
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:
                dict_objs = json.load(f)
            for obj in dict_objs.values():
                # Pick the classname
                class_name = obj["__class__"]
                # recreate class using eval() and
                # expand obj dictionary to pass all key, value
                # pairs to the __init__() of the class i.e class_name
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
