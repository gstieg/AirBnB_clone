#!/usr/bin/python3
"""unit test for User class
"""


from models.user import User
import unittest
import json
import os


class TestUser(unittest.TestCase):
    """ class User with tests """

    def setUp(self):
        """ set up """
        pass

    def test_doc(self):
        """testing docstrings exists """
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_init_arg_kwarg(self):
        """ testing passing arg/kwarg into instance """
        my_model = User(100)
        self.assertEqual(type(my_model).__name__, "User")
        self.assertFalse(hasattr(my_model, "100"))
        b1 = User(name='Gary')
        self.assertEqual(type(b1).__name__, "User")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ tests save method """
        my_model = User()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ test for attributes of User """
        my_model = User()
        new_model = User()
        self.assertTrue(isinstance(my_model, User))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_(self):
        """ tests str method """
        b1 = User()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[User] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """ tests to_dict method """
        b1 = User()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "User")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.user.User'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "User")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')


if __name__ == "__main__":
    unittest.main()
