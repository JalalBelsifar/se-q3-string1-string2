#!/usr/bin/env python3
"""
Unit tests for string2

Students should not modify this file.
"""

__author__ = 'madarp'

import sys
import unittest
import importlib
import subprocess

# Kenzie devs: change this to 'soln.string2' to test solution
PKG_NAME = 'string2'


class TestString2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_verbing(self):
        """Check if verbing function is working"""
        verbing = self.module.verbing
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swimming'), 'swimmingly')
        self.assertEqual(verbing('do'), 'do')

    def test_not_bad(self):
        """Check if not_bad function is working"""
        not_bad = self.module.not_bad
        self.assertEqual(
            not_bad('This movie is not so bad'), 'This movie is good'
            )
        self.assertEqual(
            not_bad('This dinner is not that bad!'), 'This dinner is good!'
            )
        self.assertEqual(
            not_bad('This tea is not hot'), 'This tea is not hot'
            )
        self.assertEqual(
            not_bad("It's bad yet not"), "It's bad yet not"
            )

    def test_front_back(self):
        """Check if front_back function is working"""
        front_back = self.module.front_back
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
