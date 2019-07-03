#!/usr/bin/python3
""" unittest for file storage"""

import unittest
import models
import os
import json
import time
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class test_file(unittest.TestCase):
    """ start by testing the actual file"""

    def test_setUP(self):
        FileStorage._FileStorage_objects = {}
        os.rename("file.json", "temp.json")

    def test_tearDown(self):
        FileStorage._FileStorage_objects = {}
        os.rename("temp.json", "file,json")

    def test_new_test_file(self):
        FileStorage._FileStorage_objects = {}
        self.assertEqual(models.storage.all)
        self.assertEqual(models.storage.save)
        self.assertEqual(models.storage.new)
        self.assertEqual(models.storage.reload)

    def test_all_return_type(self):
        FileStorage._FileStorage_objects = {}
        storage_return = FileStorage()
        self.assertEqual(storage_return.all(), storage_return.__dict__)
