#!/usr/bin/python3
"""A module that defines basic attributes common to all sub-modules"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel

    Description:
    This class models all attributes common to other classes
    inheriting from this.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Object

        Description:
        This attribute initializes the instance object with the id,
        date created and the date the instance object was updated

        Args:
        args (str): a variable-length argument.
        kwargs (str): a key-word variable-length argument
        """

        from models import storage
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Save Object

        Description:
        This method tracks the date the instance object was updated
        """

        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Create a Dictionary Representation

        Description:
        Creates a dictionary representation of this instance object.
        It contains the class name of the object, the date and time
        the instance object was created and last updated

        Returns:
        A dictionary representation of this model instance
        """

        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.__dict__["created_at"].isoformat()
        dict_obj["updated_at"] = self.__dict__["updated_at"].isoformat()

        return dict_obj

    def __str__(self):
        """String Representation

        Description:
        Creates a string representation of this instance object.

        Returns:
        A string representation of this model instance.
        """

        info = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return info
