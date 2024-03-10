#!/usr/bin/python3
"""A module to model a review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Model

    Description:
    Creates a new review which inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
