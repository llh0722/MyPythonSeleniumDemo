# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 17:18
# 文件       ：5-JS处理滚动条.py
# IDE        ：PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
print(driver.name)
driver.implicitly_wait(10)
driver.find_element_by_id('kw').send_keys('博客园')
driver.find_element_by_id('su').click()
time.sleep(2)
#滚动到底部
jsBottom = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(jsBottom)
time.sleep(3)
# 滚动到顶部
jsTop = "window.scrollTo(0,0)"
driver.execute_script(jsTop)

time.sleep(2)
driver.quit()