# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 14:16
# Tool ：PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://baidu.com/')

# 显示等待 元素出现
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('kw')).send_keys('yoyoketang')
# 元素消失
is_disappeared = WebDriverWait(driver, 10, 1).until_not(lambda x: x.find_element_by_id('kw').is_displayed())
print(is_disappeared)
