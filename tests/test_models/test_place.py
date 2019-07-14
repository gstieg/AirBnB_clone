#!/usr/bin/python3
"""
UnitTest for Place class
"""

from models.place import Place
import unittest
import json
import os


class TestPlace(unittest.TestCase):
    """ Place test cases """

    def setUp(self):
        """ set up """
        pass

    def test_doc(self):
        """testing docstrings"""
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_init_arg_kwarg(self):
        """ testing passing arg/kwarg into instance """
        my_model = Place(50)
        self.assertEqual(type(my_model).__name__, "Place")
        self.assertFalse(hasattr(my_model, "50"))
        b1 = Place(name='Gary')
        self.assertEqual(type(b1).__name__, "Place")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ tests save method """
        my_model = Place()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ test for attributes of Place """
        my_model = Place()
        new_model = Place()
        self.assertTrue(isinstance(my_model, Place))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_(self):
        """ testing to see if the method is printing """
        b1 = Place()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[Place] ({}) {}".format(b1.id, b1.__dict__))
    def test_before_todict(self):
        """ test the instance using the todict conversion"""
        b1 = Place()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Place")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.place.Place'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "Place")
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
