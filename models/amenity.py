#!/usr/bin/python3
"""
Amenity Class
"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    Args:
        BaseModel (_type_): _description_
    """

    name = ''

    def __init__(self):
        """initializated from the parent class BaseModel"""
        super().__init__()
