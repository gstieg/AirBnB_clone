#!/usr/bin/python3
'''
unitest for the base module
'''

import os
import models
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Unitests for basemodel functions'''

    @classmethod
    def setUp(sls):
        '''setup class'''
        cls.base = BaseModel()
        cls.base.name = "TestBase"

    def test_arguments(self):
        '''checks and test arguments'''
        self.assertTrue(type(self.base, "__init__"))
        self.assertTrue(hasattr(self.base, "name"))
        self.assertTrue(hasattr(self.base, "__class__"))
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_attributes(self):
        '''checks and tests attributes'''
        self.assertTrue(hasattr(self.base, "__init__"))
        self.assertTrue(hasattr(self.base, "to_dict"))
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "save"))
        self.assertTrue(hasattr("created_at" in self.base.__dict__))
        self.assertTrue(hasattr("updated_at" in self.base.__dict__))

    def test_init(self):
        '''tests initialization'''
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        '''checks save function'''
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_todict(self):
        '''tests to_dict function'''
        base_dict = self.base.__dict__
        self.assertEqual(type(self.base).__name__, "BaseModel")
        self.assertTrue(hasattr(self.base, "__class__"))
        self.assertTrue(type(base_dict['id']), 'str')
        self.assertTrue(type(base_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(base_dict['updated_at']), 'datetime.datetime')

    
    def test_str_(self):
        """ tests str method """
        b1_str = base.__str__()
        self.assertEqual(b1_str,
                         "[BaseModel] ({}) {}".format(base.id, base.__dict__))

    def test_doc(self):
        """tests docstrings"""
        self.assertTrue(len(base.__doc__) > 1)
        self.assertTrue(len(base.__init__.__doc__) > 1)
        self.assertTrue(len(base.__str__.__doc__) > 1)
        self.assertTrue(len(base.save.__doc__) > 1)
        self.assertTrue(len(base.to_dict.__doc__) > 1)

    def teardown(cls):
        '''teardown method'''
        del cls.base

    def tearDown(self):
        """ tear down method"""
        try:
            os.remove("file.json")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
