# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/3 11:52
# Tool ：PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
一、简单操作
1.点击（鼠标左键）页面按钮：click()
2.请空输入框：clear()
3.输入字符串：send_keys()
4.打开测试部落论坛后，点击放大镜搜索图标，一般为了保证输入的正确性，
可以先清空下输入框，然后输入搜索关键字
二、submit提交表单
1.在前面百度搜索案例中，输入关键字后，可以直接按回车键搜索，也可以点搜索按钮搜索。
2.submit()一般用于模拟回车键
三、键盘操作
1.selenium提供了一整套的模拟键盘操作事件，前面submit()方法如果不行的话，可以试试模拟键盘事件
2.模拟键盘的操作需要先导入键盘模块：from selenium.webdriver.common.keys import Keys
3.模拟enter键，可以用send_keys(Keys.ENTER)
4.其它常见的键盘操作：
键盘F1到F12：send_keys(Keys.F1) 把F1改成对应的快捷键
复制Ctrl+C：send_keys(Keys.CONTROL,'c') 
粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 
全选Ctrl+A：send_keys(Keys.CONTROL,'a') 
剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 
制表键Tab:  send_keys(Keys.TAB) 
四、鼠标悬停事件
1.鼠标不仅仅可以点击(click),鼠标还有其它的操作，如：鼠标悬停在某个元素上，
鼠标右击，鼠标按住某个按钮拖到
2.鼠标事件需要先导入模块：from selenium.webdriver.common.action_chains import ActionChains
perform() 执行所有ActionChains中的行为
move_to_element() 鼠标悬停
3.除了常用的鼠标悬停事件外，还有
右击鼠标：context_click()
双击鼠标：double_click()
'''
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(5)
# 鼠标设置悬停
mouse = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.find_element_by_id('kw').send_keys('test')
time.sleep(2)
driver.find_element_by_id('kw').clear()
time.sleep(2)
driver.find_element_by_id('kw').send_keys('测试部落')
# driver.find_element_by_id('su').click()
# submit()一般用于模拟回车键
# driver.find_element_by_id('su').submit()
# 模拟enter键，可以用send_keys(Keys.ENTER)
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()


