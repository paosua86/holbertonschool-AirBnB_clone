#!/usr/bin/python3
"""
Review Class
"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class

    Args:
        BaseModel (_type_): _description_
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self):
        """initializated from the parent class BaseModel"""
        super().__init__()
