# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 17:45
# 文件       ：6-单选框和复选框（radiobox、checkbox）.py
# IDE        ：PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///F:/config_test/radio&checkbox.html")
driver.implicitly_wait(5)
# 判断是否已选择
r1 = driver.find_element_by_id('boy').is_selected()
print(r1)
driver.find_element_by_id('boy').click()
# 判断是否已选择
r2 = driver.find_element_by_id('boy').is_selected()
print(r2)
time.sleep(2)

# 复选框单选
driver.find_element_by_id('c1').click()
time.sleep(3)
# 复选框全选
checkboxes = driver.find_elements_by_xpath('.//*[@type="checkbox"]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)
driver.quit()