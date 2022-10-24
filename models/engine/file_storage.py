#!/usr/bin/python3
"""
contains FileStorage class
"""
from models.base_model import BaseModel
import json
class_items = {"BaseModel": BaseModel}


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            dic = {}
            for key in self.__objects.keys():
                dic[key] = self.__objects[key].to_dict()
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(self.__file_path, "r") as f:
                jsonfile = json.load(f)
            for key in jsonfile:
                self.__objects[key] = class_items[jsonfile[key]["__class__"]](**jsonfile[key])
        except:
            pass

