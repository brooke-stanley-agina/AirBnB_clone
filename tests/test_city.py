#!/usr/bin/python3
"""
Module test_city
Contains unitest for City class
Which inherits from BaseModel
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class CityTestCase(unittest.TestCase):
    """
        Unit tests for City model
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup global City object
        """
        cls.obj = City()

    def test_name_is_string(self):
        """
        City's name should be an empty string
        """
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(self.obj.name, "")

    def test_state_id_is_string(self):
        """
        City's state_id should be an empty string
        """
        self.assertEqual(type(self.obj.state_id), str)
        self.assertEqual(self.obj.state_id, "")

    def test_has_inherited_attributes(self):
        """
        City model should have attributes
        id, created_at, update_at
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        Prove City is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
