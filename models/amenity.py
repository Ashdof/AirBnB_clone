#!/usr/bin/python3
"""A module to model an amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Model

    Description:
    Creates a new amenity which inherity from BaseModel
    """

    name = ""
