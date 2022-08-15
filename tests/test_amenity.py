#!/usr/bin/python3
"""
Module test_amenity
Contains unitest for Amenity class
Which inherits from BaseModel
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class AmenityTestCase(unittest.TestCase):
    """
        Unit tests for Amenity model
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup global amenity object
        """
        cls.obj = Amenity()

    def test_name_is_string(self):
        """
        Amenity's name should be an empty string
        """
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(self.obj.name, "")

    def test_has_inherited_attributes(self):
        """
        Amenity model should have attributes
        id, created_at, update_at
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        Prove Amenity is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
