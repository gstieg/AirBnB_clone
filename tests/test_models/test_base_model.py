#!/usr/bin/python3
"""
UnitTest for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import json
import os


class TestBaseModel(unittest.TestCase):
    """ Base Model test cases """

    def setUp(self):
        """ set up """
        pass

    def test_doc(self):
        """tests if docstrings exists """
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_inst_arg_kwarg(self):
        """ tests args/kwarg to an instance """
        my_model = BaseModel(20)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertFalse(hasattr(my_model, "20"))
        b1 = BaseModel(name='Gary')
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, "name"))

    def test_to_dict(self):
        """ tests the to_dict method """
        b1 = BaseModel()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_(self):
        """ tests str method """
        b1 = BaseModel()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[BaseModel] ({}) {}".format(b1.id, b1.__dict__))

    def test_attr(self):
        """ test attributes of BaseModel """
        my_model = BaseModel()
        new_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_args(self):
        """ tests arg/kwarg """
        my_model = BaseModel(20)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertFalse(hasattr(my_model, "20"))
        b1 = BaseModel(name='Gary')
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ tests save """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def tearDown(self):
        """ tear down """
        try:
            os.remove("file.json")
        except:
            pass
