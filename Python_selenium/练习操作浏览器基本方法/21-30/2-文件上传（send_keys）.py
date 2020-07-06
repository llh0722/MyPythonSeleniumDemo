# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 11:04
# Tool ：PyCharm

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://account.cnblogs.com/signin')
driver.implicitly_wait(10)
driver.maximize_window()

# 登录
driver.find_element_by_id('mat-input-0').send_keys('嗨林子哈')
driver.find_element_by_id('mat-input-1').send_keys('llh2020@.')
driver.find_element_by_class_name('mat-button-wrapper').click()

time.sleep(5)
handle = driver.current_window_handle
print(driver.title)
driver.find_element_by_link_text('写博').click()
handles = driver.window_handles
for h in handles:
    if h != handle:
        driver.switch_to.window(h)
        print(driver.title)
time.sleep(3)
driver.find_element_by_link_text('添加新随笔').click()
# 定位图片编辑器
time.sleep(3)
driver.find_element_by_css_selector('img.mceIcon').click()
# 切换iframe
iframe = driver.find_elements_by_tag_name('iframe')[1]
driver.switch_to.frame(iframe)

# 上传文件
driver.find_element_by_name('file').send_keys(r'D:\project\PycharmProjects\PythonSelenium\MyPythonSeleniumDemo\Python_selenium\picture\test-1.png')
time.sleep(3)

