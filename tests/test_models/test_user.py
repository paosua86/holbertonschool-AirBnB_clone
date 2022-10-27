#!/usr/bin/python3
"""
Unit Test for User Class
"""
from datetime import datetime
import json
import models
import unittest

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """testing for class User"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.model = User()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.model, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.model)
        my_list = ['[', ']', '(', ')']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(4 == actual)

    def test_save(self):
        """save function should add updated_at attribute"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)
        
    def test_to_dict(self):
        """save class in a dictionary"""
        dictT = type(self.model.to_dict())
        self.assertEqual(dictT, type({}))
        
    def test_email(self):
        """verified email set parameter"""
        asert = False
        if (self.model.email != None):
            asert = True
        self.assertTrue(asert)
        
    def test_password(self):
        """verified email set parameter"""
        asert = False
        if (self.model.password != None):
            asert = True
        self.assertTrue(asert)
        
    def test_first_name(self):
        """verified email set parameter"""
        asert = False
        if (self.model.first_name != None):
            asert = True
        self.assertTrue(asert)
        
    def test_last_name(self):
        """verified email set parameter"""
        asert = False
        if (self.model.last_name != None):
            asert = True
        self.assertTrue(asert)

if __name__ == '__main__':
    unittest.main
