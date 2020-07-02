# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 16:15
# Tool ：PyCharm

"""
设置窗口大小
1.可以设置浏览器窗口大小，如设置窗口大小为手机分辨率540*960
2.也可以最大化窗口
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 设置浏览器窗口大小
driver.set_window_size(540, 960)
time.sleep(3)
# 最大化窗口
driver.maximize_window()

driver.quit()
