#!/usr/bin/python3
"""
UnitTest for Amenity class
"""
from models.amenity import Amenity
import unittest
import json
import os


class TestAmenity(unittest.TestCase):
    """ Amenity test cases """

    def setUp(self):
        """ set up """
        pass

    def test_doc(self):
        """tests docstrings"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_arg_kwarg(self):
        """ testing passesd args/kwarg to instance """
        my_model = Amenity(20)
        self.assertEqual(type(my_model).__name__, "Amenity")
        self.assertFalse(hasattr(my_model, "20"))
        b1 = Amenity(name='Gary')
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ test save method """
        my_model = Amenity()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ test for attributes of Amenity """
        my_model = Amenity()
        new_model = Amenity()
        self.assertTrue(isinstance(my_model, Amenity))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_(self):
        """ tests str method """
        b1 = Amenity()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[Amenity] ({}) {}".format(b1.id, b1.__dict__))

    def test_to_dict(self):
        """ tests to_dict method """
        b1 = Amenity()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.amenity.Amenity'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "Amenity")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def tearDown(self):
        """ tear down """
        try:
            os.remove("file.json")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
