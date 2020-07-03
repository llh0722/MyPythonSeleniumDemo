# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 15:56
# Tool ：PyCharm

"""
设置休眠
1.由于打开百度网址后，页面加载需要几秒钟，所以最好等到页面加载完成后再继续下一步操作
2.导入time模块，time模块是Python自带的，所以无需下载
3.设置等待时间，单位是秒（s）,时间值可以是小数也可以是整数
"""


from selenium import webdriver  # 导入selenium的webdriver模块
import time   # 导入time模块

driver = webdriver.Chrome()   # 打开谷歌浏览器
# 打开百度网站
driver.get('http://www.baidu.com/')

# 设置休眠
time.sleep(3)

# 关闭浏览器
driver.close()
