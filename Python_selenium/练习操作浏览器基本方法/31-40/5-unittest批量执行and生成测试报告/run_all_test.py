# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 11:19
# Tool ：PyCharm

import unittest
import HTMLTestRunner
import os

u'''用例路径'''
case_path = os.path.join(os.getcwd(), 'case')
u'''报告路径'''
report_path = os.path.join(os.getcwd(), 'report')

def runAllCase():
    discover = unittest.defaultTestLoader.discover(
        case_path,
        pattern='test*.py',
        top_level_dir=None
    )

    print(discover)
    return discover

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(runAllCase())
    report_html_path = os.path.join(report_path, 'result.html')
    fp = open(report_html_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'test测试报告',
        description=u'测试用例执行情况'
        # verbosity=2,
        # retry=1
    )
    runner.run(runAllCase())
    fp.close()

