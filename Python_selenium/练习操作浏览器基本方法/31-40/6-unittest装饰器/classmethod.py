# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 12:02
# Tool ：PyCharm

import unittest

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('开始测试')

    @classmethod
    def tearDownClass(cls) -> None:
        print('结束测试')

    def test_01(self):
        u"""01启动"""
        print('01启动')

    def test_02(self):
        print('02启动')

    def test_03(self):
        print('03启动')

    def test_04(self):
        print('04启动')

if __name__ == '__main__':
    unittest.main()