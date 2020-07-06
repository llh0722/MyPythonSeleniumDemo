# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 16:58
# Tool ：PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com/')
# 判断title完全等于
title = EC.title_is(u'百度一下，你就知道')
print(title(driver))
# 判断title包含
title1 = EC.title_contains(u"百度一下")
title2 = EC.title_contains(u"百度一次")
print(title1(driver), title2(driver))


