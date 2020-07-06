# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/6 13:29
# Tool ：PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(5)


# 判断
def is_element_exit(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print('未找到元素')
        return False
    elif len(s) == 1:
        print('找到元素%s' % css)
        return True
    else:
        print('找到%s个元素%s' % (len(s), css))
        return False


if is_element_exit('#kw'):
    driver.find_element_by_id('kw').send_keys('存在呀')
if is_element_exit('input'):
    driver.find_elements_by_tag_name('input')
if is_element_exit('xxx'):
    driver.find_element_by_id('xxx').send_keys('xxx')


def isElementExit(css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False
