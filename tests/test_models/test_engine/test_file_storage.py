#!/usr/bin/python3
"""Test Filestorage"""


from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """test file storage"""

    def setUp(self):
        """setup"""
        self.file_storage = FileStorage()
