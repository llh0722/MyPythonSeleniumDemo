# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 13:48
# Tool ：PyCharm

from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://www.cnblogs.com/yoyoketang/')
driver.implicitly_wait(5)
page = driver.page_source
print(page)

url_list = re.findall('href=\"(.*?)\"', page, re.S)
url_all = []
for url in url_list:
    if 'http' in url:
        print(url)
        url_all.append(url)
print(url_all)

