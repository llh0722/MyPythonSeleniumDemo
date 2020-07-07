# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 10:52
# Tool ：PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class Blogs(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.cnblogs.com/')

    def testBlogIndex(self):
        result = EC.title_is(u'博客园 - 开发者的网上家园')(self.driver)
        self.assertTrue(result)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()