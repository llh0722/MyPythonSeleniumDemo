# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 16:05
# Tool ：PyCharm

"""
前进和后退
1.当在一个浏览器打开两个页面后，想返回上一页面，相当于浏览器左上角的左箭头按钮
2.返回到上一页面后，也可以切换到下一页，相当于浏览器左上角的右箭头按钮
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
time.sleep(3)
driver.get("http://news.baidu.com/")
driver.back()   # 回退
time.sleep(3)
driver.forward()   # 前进
time.sleep(3)

driver.quit()

