# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import xlrd

wr_file = xlrd.open_workbook(r'./x.xlsx')
sheet = wr_file.sheet_by_index(0)

rownum = sheet.nrows
colnum = sheet.ncols
if rownum > 0 and colnum > 0:
    f = open("./tim.txt", 'w', encoding="utf-8")
    for raw in range(rownum):
        strs = " "
        for cal in range(colnum):
            strs = strs + str(sheet.row(raw)[cal]).replace("text:", " ").replace("'", "").replace(",", "").replace("empty", "").replace("number", "")
            if cal + 1 == colnum:
                f.write(strs + "\n")

    else:
        pass
    f.close()

