"""
Test_secure.py

Created on Thu May  2 15:19:14 2019

@author: larry
"""
import unittest


# import secure


class TestSecure(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()