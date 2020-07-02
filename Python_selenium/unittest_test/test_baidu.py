# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/13 12:03
# Tool ：PyCharm
# 优化测试套件
import unittest
from Python_selenium.unittest_config.config import InitTest
class BaiduTest(InitTest):

    @unittest.skip('do not run')
    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
        # time.sleep(1)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        url=self.driver.current_url
        print('当前页面URL:{0}'.format(url))
        self.assertEqual(url,'http://news.baidu.com/')

    def test_baidu_title(self):
        title=self.driver.title
        self.assertTrue(title,'百度一下，你就知道')

    def test_baidu_so(self):
        so=self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()
        # time.sleep(1)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        url = self.driver.current_url
        print('当前页面URL:{0}'.format(url))
        # self.assertEqual(url, 'https://map.baidu.com/@12973149,4835925,13z')
        self.driver.get('https://www.baidu.com/')

    @staticmethod
    def suite(testCaseClass):
        suite=unittest.TestLoader().loadTestsFromTestCase(testCaseClass)
        return suite

# if __name__ == '__main__':
#     unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite(BaiduTest))
