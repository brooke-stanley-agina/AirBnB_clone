#!/usr/bin/python3
"""
Module test_review
Contains unitest for Review class
Which inherits from BaseModel
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):
    """
        Unit tests for Review model
        """

    @classmethod
    def setUpClass(cls):
        """
        Setup global Review object
        """
        cls.obj = Review()

    def test_attributes_are_strings_and_empty(self):
        """
        Review's  place_id, user_id, text
        should be empty strings
        """
        self.assertEqual(type(self.obj.place_id), str)
        self.assertEqual(self.obj.place_id, "")
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(self.obj.user_id, "")
        self.assertEqual(self.obj.text, "")
        self.assertEqual(type(self.obj.text), str)

    def test_has_inherited_attributes(self):
        """
        Review model should have inherited attributes
        id, created_at, update_at
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        Prove Review is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
