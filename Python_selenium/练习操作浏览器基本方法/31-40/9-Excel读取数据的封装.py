# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/7/7 16:00
# Tool ：PyCharm
import xlrd2


class ExcelTest(object):

    def __init__(self, excel_path, sheetName):
        # 打开文件
        self.data = xlrd2.open_workbook(excel_path)
        # 通过name获取
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行的值作为key
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNums = self.table.nrows
        # 获取总列数
        self.colNums = self.table.ncols

    def dict_data(self):
        if self.rowNums <= 1:
            print("总行数小于等于1")
        else:
            li = []
            j = 1
            for i in range(self.rowNums-1):
                s = {}
                # 获取第二行的值
                values = self.table.row_values(j)
                for x in range(self.colNums):
                    s[self.keys[x]] = values[x]
                li.append(s)
                j += 1
            return li


if __name__ == "__main__":
    excel_path = "D:\\project\\PycharmProjects\\PythonSelenium\\MyPythonSeleniumDemo\\Python_selenium\\test.xlsx"
    sheetName = "Sheet1"
    data = ExcelTest(excel_path, sheetName)
    print(data.dict_data())
