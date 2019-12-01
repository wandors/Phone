# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import xlrd

wr_file = xlrd.open_workbook(r'./x.xlsx')
sheet = wr_file.sheet_by_index(0)

inter = []
rownum = sheet.nrows
colnum = sheet.ncols
if rownum > 0 and colnum > 0:
    for raw in range(colnum):
        inter.append(str(sheet.col(raw)[0]).replace("text:", "")
                     .replace("'", "").replace(":", "").replace(",", ""))

    else:
        pass
    print(len(inter))
    print("\n".join(inter))
