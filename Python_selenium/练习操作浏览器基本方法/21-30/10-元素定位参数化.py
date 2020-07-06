# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 17:36
# Tool ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com/')

driver.find_element('id', 'kw').send_keys('博客')
driver.find_element('css selector', '#su').click()

time.sleep(3)
driver.quit()