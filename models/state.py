#!/usr/bin/python3
"""
State Class
"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """State class

    Args:
        BaseModel (_type_): _description_
    """

    name = ''

    def __init__(self):
        """initializated from the paren class BaseModel"""
        super().__init__()
