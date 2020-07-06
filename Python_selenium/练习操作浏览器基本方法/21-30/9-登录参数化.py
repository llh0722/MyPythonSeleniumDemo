# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 17:28
# Tool ：PyCharm
from selenium import webdriver
import unittest
import time
class Bolg(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print (text)
            return True
        except:
            return False

    def test_01(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"上海-悠悠", u"xxxx")  # 调用登录方法
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_02(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"上海-悠悠", u"xxxx")  # 调用登录方法
        # 判断结果   # 交流QQ群：232607095
        result = self.is_login_sucess()
        self.assertTrue(result)


    # def test_01(self):
    #     u'''登录案例参考:账号，密码自己设置'''
    #     self.login(u"上海-悠悠", u"xxxx")  # 调用登录方法
    #     # 获取登录后的账号名称
    #     text = self.driver.find_element_by_id("lnk_current_user").text
    #     print text
    #     # 断言实际结果与期望结果一致
    #     self.assertEqual(text, u"上海-悠悠")
    #
    # def test_02(self):
    #     u'''登录案例参考:账号，密码自己设置'''
    #     self.login(u"上海-悠悠", u"oooo")  # 调用登录方法
    #     # 获取登录后的账号名称
    #     text = self.driver.find_element_by_id("lnk_current_user").text
    #     print text       # 交流QQ群：232607095
    #     # 断言实际结果与期望结果一致
    #     self.assertEqual(text, u"上海-悠悠")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()