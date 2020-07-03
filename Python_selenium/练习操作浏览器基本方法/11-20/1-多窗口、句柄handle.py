# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/3 14:24
# Tool ：PyCharm
"""
有些页面的链接打开后，会重新打开一个窗口，对于这种情况，
想在新页面上操作，就得先切换窗口了。获取窗口的唯一标识用句柄表示，
所以只需要切换句柄，我们就能在多个页面上灵活自如的操作了。
switch_to_window改为switch_to.window
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(3)
# 获取当前页面窗口的句柄 driver.current_window_handle
handle = driver.current_window_handle
print(handle)
driver.find_element_by_link_text('新闻').click()
# 获取所有的句柄 window_handle
handles = driver.window_handles
print(handles)
for h in handles:
    if h != handle:
        # 切换页面
        # driver.switch_to_window(h)  switch_to_window改为switch_to.window
        driver.switch_to.window(h)
        print(driver.title)
# 关闭新页面
driver.close()
time.sleep(3)
# 切换回首页
driver.switch_to.window(handle)
print(driver.title)
driver.quit()
