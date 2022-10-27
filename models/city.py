#!/usr/bin/python3
"""
City Class
"""

import models
from models.base_model import BaseModel

class City(BaseModel):
    """City class

    Args:
        BaseModel (_type_): _description_
    """

    state_id = ''
    name = ''

    def __init__(self):
        """initializated from the parent class BaseModel"""
        super().__init__()
