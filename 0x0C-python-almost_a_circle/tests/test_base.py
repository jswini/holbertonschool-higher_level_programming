#!/usr/bin/python3
"""
test file for Base
"""
import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """
    tests for the base class
    """
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b2 = Base('a')
        self.assertEqual(b2.id, 'a')
