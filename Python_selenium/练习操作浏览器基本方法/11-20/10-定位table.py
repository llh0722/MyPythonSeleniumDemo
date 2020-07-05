# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 21:13
# 文件       ：10-定位table.py
# IDE        ：PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///F:/config_test/table.html')
driver.implicitly_wait(10)
t = driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[3]/td[1]')
print(t.text)
driver.quit()