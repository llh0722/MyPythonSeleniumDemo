# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 15:40
# Tool ：PyCharm

"""
打开网站
"""

# 导入selenium的webdriver模块
from selenium import webdriver

driver = webdriver.Chrome()   # 打开谷歌浏览器
# driver = webdriver.Ie()  打开IE浏览器
# driver = webdriver.Firefox()  打开火狐浏览器

# 打开百度网站
driver.get('http://www.baidu.com/')

# 关闭浏览器
driver.close()
