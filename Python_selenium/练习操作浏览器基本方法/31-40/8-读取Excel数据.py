# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 15:40
# Tool ：PyCharm

import xlrd2

# 打开Excel表格
data = xlrd2.open_workbook('D:\\project\\PycharmProjects\\PythonSelenium\\MyPythonSeleniumDemo\\Python_selenium\\test'
                           '.xlsx')

# 通过索引获取
# table = data.sheets()[0]
# table = data.sheet_by_index(0)
table = data.sheet_by_name(u"Sheet1")

# 获取总行数
rows = table.nrows
# 获取总列数
cols = table.ncols

print(rows, cols)
print(table.row_values(0))
print(table.row_values(1))
print(table.col_values(0))
print(table.col_values(1))

