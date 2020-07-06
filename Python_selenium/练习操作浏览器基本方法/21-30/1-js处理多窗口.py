# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 21:23
# 文件       ：1-js处理多窗口.py
# IDE        ：PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(10)
# 点击新闻进行跳转会出现新的窗口，去掉新闻链接的属性target="_blank"
jsBlank = "document.getElementsByClassName('mnav').target=''"
driver.execute_script(jsBlank)
driver.find_element_by_link_text('新闻').click()
print(driver.title)
driver.quit()