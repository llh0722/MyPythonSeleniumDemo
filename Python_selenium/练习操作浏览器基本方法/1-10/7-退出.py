# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/2 17:48
# Tool ：PyCharm

"""
退出
1.退出有两种方式，一种是close;另外一种是quit
2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口
3.quit用于结束进程，关闭所有的窗口
4.最后结束测试，要用quit。quit可以回收c盘的临时文件
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.get("http://www.sina.com/")
driver.close()
time.sleep(3)
# driver.quit()
