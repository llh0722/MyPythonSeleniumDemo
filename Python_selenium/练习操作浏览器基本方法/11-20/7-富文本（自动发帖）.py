# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 18:16
# 文件       ：7-富文本（自动发帖）.py
# IDE        ：PyCharm

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://account.cnblogs.com/signin')
driver.implicitly_wait(10)
driver.maximize_window()

# 登录
driver.find_element_by_id('mat-input-0').send_keys('嗨林子哈')
driver.find_element_by_id('mat-input-1').send_keys('llh2020@.')
driver.find_element_by_class_name('mat-button-wrapper').click()

time.sleep(5)
handle = driver.current_window_handle
print(driver.title)
driver.find_element_by_link_text('写博').click()
handles = driver.window_handles
for h in handles:
    if h != handle:
        driver.switch_to.window(h)
        print(driver.title)
time.sleep(3)
driver.find_element_by_link_text('添加新随笔').click()
# 输入博客标题
driver.find_element_by_id('post-title').send_keys('富文本测试呀')
# 切换iframe
iframe = driver.find_element_by_id('Editor_Edit_EditorBody_ifr')
driver.switch_to.frame(iframe)
driver.find_element_by_id('tinymce').send_keys(Keys.TAB)
driver.find_element_by_id('tinymce').send_keys('富文本编辑呀')




