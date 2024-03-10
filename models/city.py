#!/usr/bin/python3
"""A module to model a city"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Model

    Description:
    Creates a new city which inherits from BaseModel
    """

    state_id = ""
    name = ""
