#!/usr/bin/python3
""" BaseModel unittest class"""
import unittest
from models.base_model import BaseModel



class Test_BaseModel(unittest.TestCase):
    """Test BaseModel class"""

    @classmethod
    def test_classSetup(self):
        self.my_model = BaseModel()
        self.my_model.name = "School"
        self.my_model.my_number = 89
        self.my_model.save()
        self.dic = self.my_model.to_dict()
        self.my_new_model = BaseModel(**self.dic)
        self.assertEqual(self.dic["updated_at"], self.my_model.updated_at.isoformat())
        self.assertIsNotNone(BaseModel.__str__.__doc__)

