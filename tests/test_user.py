#!/usr/bin/python3
"""
Module test_user
Contains unitest for User class
Which inherits from BaseModel
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class UserTestCase(unittest.TestCase):
    """
       Unit tests for User model
       """

    @classmethod
    def setUpClass(cls):
        """
        Setup global User object
        """
        cls.obj = User()

    def test_has_inherited_attributes(self):
        """
        User model should have attributes
        id, created_at, update_at
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        Prove User is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_non_inheritted_atts_exists(self):
        """
        Non inherited attributes(atts) should exist
        """
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))


if __name__ == '__main__':
    unittest.main()
