#!/usr/bin/python3
"""
UnitTest for Review class
"""
from models.review import Review
import unittest
import json
import os


class TestReview(unittest.TestCase):
    """ class Review with tests """

    def setUp(self):
        """ set up """
        pass

    def tearDown(self):
        """ tear down """
        try:
            os.remove("file.json")
        except:
            pass

    def test_doc(self):
        """tests docstrings """
        self.assertTrue(len(Review.__doc__) > 1)
        self.assertTrue(len(Review.__init__.__doc__) > 1)
        self.assertTrue(len(Review.__str__.__doc__) > 1)
        self.assertTrue(len(Review.save.__doc__) > 1)
        self.assertTrue(len(Review.to_dict.__doc__) > 1)

    def test_init_arg_kwarg(self):
        """ testing passing arg/kwarg into instance """
        my_model = Review(20)
        self.assertEqual(type(my_model).__name__, "Review")
        self.assertFalse(hasattr(my_model, "20"))
        b1 = Review(name='Gary')
        self.assertEqual(type(b1).__name__, "Review")
        self.assertTrue(hasattr(b1, "name"))

    def test_save(self):
        """ tests save method"""
        my_model = Review()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ tests for attributes of Review """
        my_model = Review()
        new_model = Review()
        self.assertTrue(isinstance(my_model, Review))
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_(self):
        """ tests str method """
        b1 = Review()
        b1_str = b1.__str__()
        self.assertEqual(b1_str,
                         "[Review] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """ tests to_dict method """
        b1 = Review()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Review")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.review.Review'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')
        test_dict = b1.to_dict()
        self.assertEqual(test_dict['__class__'], "Review")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')


if __name__ == "__main__":
    unittest.main()
