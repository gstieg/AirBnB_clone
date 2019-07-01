#!/usr/bin/python3
"""
file class for storage
"""
import json

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
    instances """

    __file_path = "file.json"
    __objects = {}

    def all(self, id=None):
        """returns the dictionary __objects"""
        if id != None:
            return self.__objects
        else:
            

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
