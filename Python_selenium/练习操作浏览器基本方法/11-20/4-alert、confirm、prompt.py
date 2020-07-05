# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 16:33
# 文件       ：4-alert、confirm、prompt.py
# IDE        ：PyCharm

from selenium import webdriver
import time

url = "file:///F:/config_test/alert.html"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# alert
driver.find_element_by_id('alert').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()  # 接受
# alert.dismiss()  # 取消或X掉弹框
time.sleep(2)

# confirm
driver.find_element_by_id('confirm').click()
confirm = driver.switch_to.alert
print(confirm.text)
time.sleep(2)
confirm.accept()
# confirm.dismiss()
time.sleep(2)

# prompt
driver.find_element_by_id('prompt').click()
prompt = driver.switch_to.alert
print(prompt.text)
time.sleep(2)
prompt.send_keys('hello 月月')
print(prompt.text)
confirm.accept()
# confirm.dismiss()
time.sleep(2)
driver.quit()