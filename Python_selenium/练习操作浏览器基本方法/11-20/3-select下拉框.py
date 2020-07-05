# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 15:05
# 文件       ：3-select下拉框.py
# IDE        ：PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "http://www.baidu.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
# 定位到设置，点击搜索设置,定位高级搜索
mouse = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
# 定位下拉框--分两步定位，先定位到select框，再定位到选项
driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[3]').click()
# driver.find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[1]/span').find_element_by_xpath('//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[3]').click()
time.sleep(5)
driver.quit()