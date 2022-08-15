#!/usr/bin/python3
"""
Module review
Inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
