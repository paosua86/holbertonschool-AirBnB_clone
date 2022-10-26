#!/usr/bin/python3
"""
User Class
"""

import models
from models.base_model import BaseModel

class User(BaseModel):
    """User class

    Args:
        BaseModel (_type_): _description_
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
