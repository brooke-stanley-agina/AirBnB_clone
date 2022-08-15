#!/usr/bin/python3
"""
Module test_place
Contains unitest for Place class
Which inherits from BaseModel
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class PlaceTestCase(unittest.TestCase):
    """
       Unit tests for Place model
       """

    @classmethod
    def setUpClass(cls):
        """
        Setup global Place object
        """
        cls.obj = Place()

    def test_has_inherited_attributes(self):
        """
        Pace model should have all inherited
        attributes from base model
        """
        self.assertIn('id', self.obj.__dict__)
        self.assertIn('created_at', self.obj.__dict__)
        self.assertIn('updated_at', self.obj.__dict__)

    def test_is_subclass(self):
        """
        Prove Place is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel), True)

    def test_correct_attribute_type(self):
        """
        Attributes should have correct type
        """
        self.assertEqual(type(self.obj.city_id), str)
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(type(self.obj.description), str)
        self.assertEqual(type(self.obj.number_rooms), int)
        self.assertEqual(type(self.obj.number_bathrooms), int)
        self.assertEqual(type(self.obj.max_guest), int)
        self.assertEqual(type(self.obj.price_by_night), int)
        self.assertEqual(type(self.obj.latitude), float)
        self.assertEqual(type(self.obj.longitude), float)
        self.assertEqual(type(self.obj.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
