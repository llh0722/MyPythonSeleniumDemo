# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 19:09
# Tool ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.maximize_window()
# 设置等待
driver.implicitly_wait(5)

# 输入用户名
driver.find_element_by_id("login_field").send_keys("llh0722")
# 输入密码
driver.find_element_by_id("password").send_keys("llh653903")
# 点击登录
driver.find_element_by_name("commit").click()

time.sleep(5)

'''
验证登录是否正确
'''
driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
time.sleep(1)
text = driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong").text
print("获取我的账号名称:%s" % text)
if text == "llh0722":
    print("login success")
else:
    print("login failed")

time.sleep(2)
'''
退出登录
'''
driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/form/button").click()
driver.quit()



