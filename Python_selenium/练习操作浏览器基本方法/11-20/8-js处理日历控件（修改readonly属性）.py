# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 19:05
# 文件       ：8-js处理日历控件（修改readonly属性）.py
# IDE        ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')
driver.implicitly_wait(10)

# 定位到日历控件,移除readonly属性
jsRemove = "document.getElementById('train_date').removeAttribute('readonly')"
driver.execute_script(jsRemove)
# 输入日期,先清空输入框
'''
driver.find_element_by_id('train_date').clear()
driver.find_element_by_id('train_date').send_keys('2020-07-05')
'''
# 使用js输入日期
jsDate = "document.getElementById('train_date').value='2020-07-06'"
driver.execute_script(jsDate)
time.sleep(5)
driver.quit()