# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 14:27
# Tool ：PyCharm

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(5)

try:
    driver.find_element_by_id('kw').send_keys('博客园')
    su = driver.find_element('id', 'suxx')
except NoSuchElementException as msg:
    print(u"查找元素异常--%s" % msg)
else:
    su.click()
time.sleep(3)
driver.quit()
