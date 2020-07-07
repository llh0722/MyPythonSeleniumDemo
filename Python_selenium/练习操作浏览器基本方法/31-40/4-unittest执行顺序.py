# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 11:05
# Tool ：PyCharm

import unittest

class SxTest(unittest.TestCase):

    def setUp(self) -> None:
        print('setup')

    def test_01(self):
        print('01')

    def test_03(self):
        print('03')

    def test_02(self):
        print('02')

    def addtest(self):
        print('add')

    def tearDown(self) -> None:
        print('tearDown')

if __name__ == "__main__":
    unittest.main()