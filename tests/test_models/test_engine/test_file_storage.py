#!/usr/bin/python3
""" unittest for file storage"""

import unittest
import models
import os
import json
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
        os.rename("temp.json", "file,json")

    def test_new_test_file(self):
        self.assertTrue(models.storage.all)
        self.assertTrue(models.storage.save)
        self.assertTrue(models.storage.new)
        self.assertTrue(models.storage.reload)

    def test_all_return_type(self):
        storage_return = FileStorage()
        self.assertEqual(storage_return.all(), storage_return.__dict__)
