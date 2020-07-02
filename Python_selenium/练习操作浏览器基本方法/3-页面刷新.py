# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 15:59
# Tool ：PyCharm

"""
页面刷新
1.有时候页面操作后，数据可能没及时同步，需要重新刷新
2.这里可以模拟刷新页面操作，相当于浏览器输入框后面的刷新按钮
"""

from selenium import webdriver  # 导入selenium的webdriver模块
import time   # 导入time模块

driver = webdriver.Chrome()   # 打开谷歌浏览器
# 打开百度网站
driver.get('http://www.baidu.com/')

# 设置休眠
time.sleep(3)

try:
    driver.refresh()   # 页面的刷新refresh
    print("refresh test is successful")
except Exception as e:
    print("refresh test is fail", format(e))

# 关闭浏览器
driver.close()
