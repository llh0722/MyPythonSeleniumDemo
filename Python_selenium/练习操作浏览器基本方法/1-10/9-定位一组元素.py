# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 21:30
# Tool ：PyCharm

"""
定位一组元素find_elements
"""

from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(3)
driver.find_element_by_id('kw').send_keys('测试部落')
driver.find_element_by_id('su').click()
time.sleep(3)
# 定位一组元素
result = driver.find_elements_by_css_selector('h3.t>a')
print(result)
for re in result:
    print(re.get_attribute("href"))
t = random.randint(0, 9)
print(t)
result[t].click()
time.sleep(2)
driver.quit()
