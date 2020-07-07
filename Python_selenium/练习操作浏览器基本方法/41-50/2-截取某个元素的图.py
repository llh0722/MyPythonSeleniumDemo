# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 18:37
# Tool ：PyCharm

from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

driver.save_screenshot('button.png')
element = driver.find_element_by_id("su")
print(element.location)                # 打印元素坐标
print(element.size)                    # 打印元素大小

left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']

im = Image.open('button.png')
im = im.crop((left, top, right, bottom))
im.save('button.png')