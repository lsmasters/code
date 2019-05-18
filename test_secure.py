"""
Test_secure.py

Created on Thu May  2 15:19:14 2019

@author: larry
"""

import unittest
from secure import subs, unSubs, shift, unShift, getShift26
from unittest import mock


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

    #unit test for the handling of the shift routine: correct input
    def test_getShift26(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 3
        self.assertEqual(getShift26(), 3)

    # unit test for the handling of the shift routine: input < 1
    def test_getShift26B(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: -3      #input too small
        self.assertRaises(ValueError, getShift26)

    # unit test for the handling of the shift routine: input > 25
    def test_getShift26C(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 34   #input too large
        self.assertRaises(ValueError, getShift26)

    def test_getShift26D(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 0.345  #float input
        self.assertRaises(ValueError, getShift26)

    def test_getShift26E(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 'abc'  #string input
        self.assertRaises(ValueError, getShift26)

    def test_getShift26F(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 3 + 4j  #complex number input
        self.assertRaises(TypeError, getShift26)

    #unit test for shift() algorithm
    def test_shift(self):
        self.assertEqual(shift("abcdefg",3), "defghij")

    def test_shift2(self):
        self.assertEqual(shift("abcdefg", 5), "fghijkl")

    # unit test for unShift() algorithm
    def test_unShift2(self):
        self.assertEqual(unShift("fghijkl", 5), "abcdefg")

    # integration test for shift() and unShift()
    def test_shift_unShift(self):
        self.assertEqual("abcdefgh", unShift(shift("abcdefgh", 4), 4))

    def test_shift_unShift2(self):
        self.assertEqual("abcdefgh", unShift(shift("abcdefgh", 14), 14))

if __name__ == '__main__':
    unittest.main()
