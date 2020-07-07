# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 10:41
# Tool ：PyCharm

import unittest

class MathTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def testAdd(self):
        self.assertEqual((2+3), 5)

    def testMinus(self):
        result = 9-4
        hope = 5
        self.assertEqual(result, hope)

    def testMultiply(self):
        self.assertEqual((4*6), 24)

    def testDivide(self):
        result = 7/2
        hope = 3.5
        self.assertEqual(result, hope)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
