# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/9 16:56
# Tool ：PyCharm
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get('http://www.baidu.com/')
time.sleep(2)
url=driver.current_url
print('当前页面URL:{0}'.format(url))
driver.find_element_by_link_text('新闻').click()
time.sleep(6)
handle=driver.window_handles
driver.switch_to.window(handle[1])
url1=driver.current_url
print('当前页面URL1:{0}'.format(url1))
# print('获取到的浏览器:{0}'.format(driver.name))
# res=driver.find_element_by_id('kw')
# res.send_keys('selenium')
# time.sleep(1)
# print('百度搜索输入框的关键字：{0}'.format(res.get_attribute('value')))
# # res.clear()
# time.sleep(3)

driver.quit()



# time.sleep(2)
# driver.get('https://www.sina.com.cn/')
# time.sleep(2)
# # 后退
# driver.back()
# print('当前页面地址:{0}'.format(driver.current_url))
# time.sleep(2)
# driver.forward()
# print('当前页面地址:{0}'.format(driver.current_url))
# 获取当前页面的测试地址
# print('测试地址:{0}'.format(driver.current_url))
# 获取当前页面的代码
# print('页面代码:{0}'.format(driver.page_source).encode('utf-8'))
# 获取当前页面标题
# print('页面标题:{0}'.format(driver.title))
# driver.find_element_by_id('su').click()
# driver.refresh()  # 刷新