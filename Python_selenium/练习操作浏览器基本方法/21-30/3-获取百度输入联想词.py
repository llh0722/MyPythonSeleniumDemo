# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 11:30
# Tool ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(5)
driver.find_element_by_id('kw').send_keys('博客')
time.sleep(3)
bd = driver.find_elements_by_class_name('bdsug-overflow')
for i in bd:
    print(i.get_attribute('data-key'))
time.sleep(2)
if len(bd) > 1:
    bd[1].click()
    print(driver.current_url)
else:
    print('没有匹配的联想词')
time.sleep(2)
driver.quit()
