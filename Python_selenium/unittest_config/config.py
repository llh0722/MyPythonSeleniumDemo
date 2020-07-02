# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/14 14:42
# Tool ：PyCharm

import unittest
from selenium import webdriver

class InitTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()