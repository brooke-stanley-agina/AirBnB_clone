#!/usr/bin/python3
"""
Module test_state
Contains unitest for State class
Which inherits from BaseModel
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class StateTestCase(unittest.TestCase):
    """
        Unit tests for State model
        """

    @classmethod
    def setUpClass(cls):
        """
        Setup global State object
        """
        cls.obj = State()

    def test_name_is_string(self):
        """
        State's name should be an empty string
        """
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(self.obj.name, "")

    def test_has_inherited_attributes(self):
        """
        State model should have attributes
        id, created_at, update_at
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        State is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
