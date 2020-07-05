# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/3 14:51
# Tool ：PyCharm
"""
介绍switch_to_frame使用方法
一、frame和iframe区别
    Frame与Iframe两者可以实现的功能基本相同，不过Iframe比Frame具有更多的灵活性。
frame是整个页面的框架，iframe是内嵌的网页元素，也可以说是内嵌的框架
    Iframe标记又叫浮动帧标记，可以用它将一个HTML文档嵌入在一个HTML中显示。它和
Frame标记的最大区别是在网页中嵌入 的<Iframe></Iframe>所包含的内容与整个页面是
一个整体，而<Frame>< /Frame>所包含的内容是一个独立的个体，是可以独立显示的。另
外，应用Iframe还可以在同一个页面中多次显示同一内容，而不必重复这段内 容的代码。
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://mail.163.com/")
driver.maximize_window()
driver.implicitly_wait(30)
'''
1.由于登录按钮是在iframe上，所以第一步需要把定位器切换到iframe上
2.用switch_to_frame方法切换，此处有id属性，可以直接用id定位切换切换到iframe
'''
# driver.switch_to.frame("x-URS-iframe1593786854041.447")
iframe = driver.find_element_by_xpath('//*[@id="x-URS-iframe1593845773727.1487"]')
driver.switch_to.frame(iframe)
driver.find_element_by_name("email").send_keys("17600275312")
time.sleep(2)
driver.find_element_by_name("password").send_keys("llh")
time.sleep(2)
# 切换出去
driver.switch_to.default_content()
time.sleep(3)
driver.quit()