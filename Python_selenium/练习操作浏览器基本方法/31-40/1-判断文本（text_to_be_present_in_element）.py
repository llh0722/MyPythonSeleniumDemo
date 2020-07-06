# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 18:01
# Tool ：PyCharm
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

url = "http://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)
text = driver.find_element_by_id('virus-2020').text
print(text)
locator = ('id', 'virus-2020')
text1 = '高考加油'
result1 = EC.text_to_be_present_in_element(locator, text1)(driver)
print(result1)

text2 = '赤虎'
result2 = EC.text_to_be_present_in_element(locator, text2)(driver)
print(result2)

time.sleep(2)
driver.quit()