#!/usr/bin/python3
"""A module to model a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Model

    Description:
    Creates a new user which inherits from the BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
