#!/usr/bin/python3
""" State unittest class"""
import unittest
import json
import pep8
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage


class Test_State(unittest.TestCase):
    """Test State class"""
    
    @classmethod
    def classSetup(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.....  For State Class  .....')
        print('.................................\n\n')

    def setUp(self):
        """initializes new BaseModel instance for testing"""
        self.model = State()

    def test_instantiation(self):
        """ checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, State)

    def test_to_string(self):
        """checks if BaseModel  is properly casted to string"""
        my_str = str(self.model)
        my_list = ['[', ']', '(', ')']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(4 == actual)

    def test_pep8_state(self):
        """... state.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/state.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)
        
    def test_save(self):
        """save function should add updated_at attribute"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    """
    RUN TESTS
    """
    unittest.main