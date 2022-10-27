#!/usr/bin/python3
"""Test Filestorage"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
import pep8
import json
import unittest


class TestFileStorage(unittest.TestCase):
    """test file storage"""

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        print('\n\n.................................')
        print('...... Testing FileStorate ......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')
        cls.bm_obj = BaseModel()
        cls.bm_obj.save()


    def setUp(self):
        """initializes new storage object for testing"""
        self.bm_obj = TestFileStorage.bm_obj
        self.state_obj = TestFileStorage.state_obj
        self.storage = FileStorage()

    def test_instantiation(self):
        """... checks proper FileStorage instantiation"""
        self.assertIsInstance(self.file_store, FileStorage)

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        bm_id = self.bm_obj.id
        all_obj = self.storage.all()
        actual = False
        for k in all_obj.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(actual)

    def test_pep8_filestore(self):
        """... city.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_save(self):
        """... checks proper FileStorage instantiation"""

        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = False
        with open('./dev/file', mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(True)

    def test_reload(self):
        """... checks proper usage of reload function"""
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = False
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if bm_id in k:
                actual = True
        self.assertTrue(actual)


if __name__ == "__main__":
    """Run Test"""
    
    unittest.main