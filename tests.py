import unittest
import tempfile
import os

from funcs import (
    is_binary_string,
    find_binaries_in_text,
    find_binaries_in_file,
)


class TestBinaryUtils(unittest.TestCase):
    def test_is_binary_string_valid(self):
        self.assertTrue(is_binary_string("0"))
        self.assertTrue(is_binary_string("1"))
        self.assertTrue(is_binary_string("1010"))
        self.assertTrue(is_binary_string("000111"))
        self.assertTrue(is_binary_string("   1011   "))
