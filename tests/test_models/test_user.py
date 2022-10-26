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
        self.user = User()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.user)
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

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.user_json = self.user.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.user_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

if __name__ == '__main__':
    unittest.main
