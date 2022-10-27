#!/usr/bin/python3
"""
Unit Test for User Class
"""
from datetime import datetime
import json
import models
import unittest

User = models.user.User
BaseModel = models.base_model.BaseModel


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

if __name__ == '__main__':
    unittest.main
