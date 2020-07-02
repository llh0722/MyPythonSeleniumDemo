# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/13 12:03
# Tool ：PyCharm
import unittest
from selenium import webdriver
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

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

class BaiduMapTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()
        # time.sleep(1)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
        url = self.driver.current_url
        print('当前页面URL:{0}'.format(url))
        # self.assertEqual(url, 'https://map.baidu.com/@12973149,4835925,13z')
        self.driver.get('https://www.baidu.com/')


# if __name__ == '__main__':
    '''
    按添加顺序执行
    suite=unittest.TestSuite()
    suite.addTest(BaiduTest('test_baidu_news'))
    suite.addTest(BaiduTest('test_baidu_map'))
    '''
    '''
    按测试类执行
    suite=unittest.TestSuite(unittest.makeSuite(BaiduTest))
    '''
    '''
    加载测试类执行
    suite=unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    '''
    # 按测试模块执行
    # suite=unittest.TestLoader().loadTestsFromModule('unittest_test.py')
    # unittest.TextTestRunner(verbosity=2).run(suite)
