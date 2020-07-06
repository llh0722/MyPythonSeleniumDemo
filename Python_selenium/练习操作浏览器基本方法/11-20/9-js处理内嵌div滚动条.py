# _*_coding:utf-8_*_
# 作者       ：${刘林豪} 
# 创建时间   ：下午 20:50
# 文件       ：9-js处理内嵌div滚动条.py
# IDE        ：PyCharm

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///F:/config_test/js_div_gdt.html')
driver.implicitly_wait(10)
# 纵向滚动-向下滚动到底部
jsBottom = "document.getElementById('yoyoketang').scrollTop=100000"
driver.execute_script(jsBottom)
time.sleep(5)
# 纵向滚动-向下滚动到顶部
jsTop = "document.getElementById('yoyoketang').scrollTop=0"
driver.execute_script(jsTop)
time.sleep(3)
# 横向滚动-右侧
jsRight = "document.getElementById('yoyoketang').scrollLeft=10000"
driver.execute_script(jsRight)
time.sleep(3)
# 横向滚动-左侧
jsLeft = "document.getElementById('yoyoketang').scrollLeft=0"
driver.execute_script(jsLeft)
time.sleep(3)
driver.quit()