# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 16:48
# Tool ：PyCharm
from selenium import webdriver
import time, unittest
from selenium.webdriver.support import expected_conditions as EC


class BaiduTest(unittest.TestCase):

    def setUp(self) -> None:
        url = "http://www.baidu.com/"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def test_01(self):
        try:
            self.driver.find_element_by_id('kw').send_keys('测试部落')
            self.driver.find_element_by_id('suxx').click()
            time.sleep(3)
            title = EC.title_is(u"测试部落_百度搜索")(self.driver)
            self.assertFalse(title)
        except Exception as msg:
            print("异常原因:%s" % msg)
            # 时间戳
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            file_path = "D:\\project\\PycharmProjects\\PythonSelenium\\MyPythonSeleniumDemo\\Python_selenium\\picture\\"
            # 截图
            self.driver.get_screenshot_as_file((file_path + "%s.png") % nowtime)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
