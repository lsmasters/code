"""
Test_secure.py

Created on Thu May  2 15:19:14 2019

@author: larry
"""

import unittest
#from unittest import mock    not needed right now
#import secure

class TestSecure(unittest.TestCase):
    #tests for the substitution algorithm for encode and decode
    def test_SubsUnsubsText(self):
        t = "This is a test of the substitution algorithm."
        self.assertEqual(t.upper(), secure.unSubs(secure.subs(t)))

    def test_SubsUnSubsNumbers(self):
        n = "This is a test with numbers.  1 5 3 7 0"
        self.assertEqual(n.upper(), secure.unSubs(secure.subs(n)))

    def test_SubsUnSubsSynbols(self):
        s = "This is a test with symbols. !@#$%^&*()"
        self.assertEqual(s.upper(), secure.unSubs(secure.subs(s)))

    def test_SubsUnSubsMixed(self):
        m = "This is a test with all. ? ! 1 4 7 3 9 2 45 ^ @"
        self.assertEqual(m.upper(), secure.unSubs(secure.subs(m)))
    """""
    #Test for the handling of the shift routine
    def test_getShift(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 3
        self.assertEqual(secure.getShift(), 3)

    #test for the shift algorithm
    def test_Shift_unShift(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 3
        self.assertEqual(secure.shift("abcdefg"), "defghij")

    def test_Shift_unShift2(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: 5
        self.assertEqual(secure.shift("abcdefg"), "fghijkl")
    """
if __name__ == '__main__':
    unittest.main()