#!/usr/bin/python3
"""
Module city
Inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    name = ""
    state_id = ""
