#!/usr/bin/python3
"""
UnitTest for City class
"""


from models.city import City
import unittest
import json
import os


class TestCity(unittest.TestCase):
    """ City class test cases"""

    def setUp(self):
        """ set up """
        pass

    def test_doc(self):
        """testing docstrings exists """
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_init_arg_kwarg(self):
        """ testing passing arg/kwarg into instance """
        my_model = City(25)
        self.assertEqual(type(my_model).__name__, "City")
        self.assertFalse(hasattr(my_model, "25"))
        b1 = City(name='San Francisco')
        self.assertEqual(type(b1).__name__, "City")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ test if current datetime is updated """
        my_model = City()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ test for attributes of City """
        my_model = City()
        new_model = City()
        self.assertTrue(isinstance(my_model, City))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_(self):
        """ testing to see if the method is printing """
        b1 = City()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[City] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """ test the instance using the todict conversion"""
        b1 = City()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "City")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.city.City'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "City")
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
