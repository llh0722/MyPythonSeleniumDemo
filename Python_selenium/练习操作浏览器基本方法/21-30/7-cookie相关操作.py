# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 15:37
# Tool ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.get_cookies())
driver.get('https://www.cnblogs.com/')
print('登录前的cookies', driver.get_cookies())
print('登录前的指定cookie', driver.get_cookie(name='.CNBlogsCookie'))
driver.get('https://account.cnblogs.com/signin')
# 登录
driver.find_element_by_id('mat-input-0').send_keys('嗨林子哈')
driver.find_element_by_id('mat-input-1').send_keys('llh2020@.')
driver.find_element_by_class_name('mat-button-wrapper').click()
time.sleep(3)
print('登录后的cookies', driver.get_cookies())
print('登录后指定的cookie', driver.get_cookie(name='.CNBlogsCookie'))
time.sleep(3)

# 清除cookies
driver.delete_cookie(name='.CNBlogsCookie')
print('清除后的cookies', driver.get_cookies())
driver.refresh()
time.sleep(3)
driver.quit()