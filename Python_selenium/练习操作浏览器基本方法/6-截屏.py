# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 17:25
# Tool ：PyCharm

"""
截屏
1.打开网站之后，也可以对屏幕截屏
2.截屏后设置制定的保存路径+文件名称+后缀
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
time.sleep(3)
driver.get_screenshot_as_file("D:\\project\PycharmProjects\\PythonSelenium\\MyPythonSeleniumDemo\\Python_selenium"
                              "\\picture\\test-1.png")
time.sleep(2)
driver.quit()
