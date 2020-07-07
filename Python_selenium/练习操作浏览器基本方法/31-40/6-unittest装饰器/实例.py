# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 14:05
# Tool ：PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


class BlogsHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        url = 'https://www.cnblogs.com/'
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.get(url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_01(self):
        u"""验证元素存在：代码改变世界"""
        locator = ('id', 'site_nav_top')
        text = u'代码改变世界'
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_02(self):
        u"""验证title：博客园 - 开发者的网上家园"""
        title = self.driver.title
        result = EC.title_is(title)(self.driver)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
