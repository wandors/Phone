# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os
import xlrd


class Main:
    pathE = "./Деталізація витрат.xlsx"
    patht = "./telss.txt"
    pathv = "./tim.txt"
    listel = []
    imters = []

    def __init__(self):
        self.wr_file = xlrd.open_workbook(self.pathE)
        self.sheet = self.wr_file.sheet_by_index(0)
        self.rownum = self.sheet.nrows
        self.colnum = self.sheet.ncols
        if self.rownum > 0 and self.colnum > 0:
            self.f = open(self.pathv, 'w', encoding="utf-8")
            for raw in range(self.rownum):
                self.strs = " "
                for cal in range(self.colnum):
                    self.strs = self.strs + str(self.sheet.row(raw)[cal]).replace("text:", " ").replace("'", "").replace(",",
                                                                                                          "").replace(
                        "empty", "").replace("number", "")
                    if cal + 1 == self.colnum:
                        self.f.write(self.strs + "\n")
            else:
                pass
            self.f.close()

        self.ff = open(self.pathv, mode="r", encoding="utf-8")
        self.textv = self.ff.read().replace("\n", ' ')
        self.ff.close()
        self.textv = self.textv.replace('\t', ' ')
        self.ff = open(self.patht, 'r')
        self.textt = self.ff.readlines()
        self.ff.close()

    def worck(self):
        self.results = []
        self.text = len(self.textv)
        for i in self.textt:
            self.listel.append(i.replace('\n', ''))
        for self.tels in self.listel:
        	self.telo = self.textv.find(self.tels)
        	while self.telo > 0:
        		self.results.append(self.telo)
        		self.telo = self.textv.find(self.tels, self.telo + len(self.tels))
        for i in self.results:
            print("-------------------------------------")
            self.textsa = str(self.textv[i-23: i-4])
            self.textse = str(self.textv[i-2: i+58]).replace(":", " ")
            print("{0} {1}".format(self.textsa, self.textse))
        os.remove(self.pathv)
    



if __name__ == '__main__':
    m = Main()
    m.worck()
