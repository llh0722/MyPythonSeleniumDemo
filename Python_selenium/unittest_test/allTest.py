# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/5/14 16:06
# Tool ：PyCharm

import unittest
import os
import time
import HTMLTestRunner

def allTest():
    '''获取所有要执行的测试用例'''
    suite=unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(__file__)),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fileName=os.path.join(os.path.dirname(__file__),'report',
                          getNowTime()+'report.html')
    fp=open(fileName,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='UI自动化测试详细报告'
    )
    runner.run(allTest())

if __name__ == '__main__':
    run()