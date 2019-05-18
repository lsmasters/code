"""
Test_secure.py

Created on Thu May  2 15:19:14 2019

@author: larry
"""

import unittest
from secure import subs, unSubs, shift, unShift, getShift26
#from unittest import mock


class TestSecure(unittest.TestCase):

    #integration tests for the substitution algorithm for encode and decode stages
    def test_SubsUnsubsText(self):
        t = "This is a test of the substitution algorithm."
        self.assertEqual(t.upper(), unSubs(subs(t)))

    def test_SubsUnSubsNumbers(self):
        n = "This is a test with numbers.  1 5 3 7 0"
        self.assertEqual(n.upper(), unSubs(subs(n)))

    def test_SubsUnSubsSynbols(self):
        s = "This is a test with symbols. !@#$%^&*()"
        self.assertEqual(s.upper(), unSubs(subs(s)))

    def test_SubsUnSubsMixed(self):
        m = "This is a test with all. ? ! 1 4 7 3 9 2 45 ^ @"
        self.assertEqual(m.upper(), unSubs(subs(m)))
    """""
    #unit test for the handling of the shift routine
    def test_getShift(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 3
        self.assertEqual(secure.getShift(), 3)
    """
    #unit test for shift()
    def test_shift(self):
        self.assertEqual(shift("abcdefg",3), "defghij")

    def test_shift2(self):
        self.assertEqual(shift("abcdefg", 5), "fghijkl")


if __name__ == '__main__':
    unittest.main()
