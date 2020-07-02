# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/12 14:26
# Tool ：PyCharm
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://mail.sina.com.cn/')
now_handle=driver.current_window_handle
driver.find_element_by_link_text('注册').click()
time.sleep(2)
handles=driver.window_handles
for handle in handles:
    if handle != now_handle:
        driver.switch_to.window(handle)
        driver.find_element_by_name('email').send_keys('cs')
        time.sleep(2)
        driver.close()
driver.switch_to.window(now_handle)
time.sleep(2)
driver.find_element_by_id('freename').send_keys('cs')
time.sleep(2)
driver.quit()