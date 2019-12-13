# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'

import sys
import os
import xlrd
import zipfile



class Main:
    pathE = "Деталізація витрат.xlsx"
    patht = "./telss.txt"
    pathv = "./tim.txt"
    pathen = os.environ["USERPROFILE"] + '/Downloads'
    listel = []
    imters = []

    def __init__(self):
        for i in os.listdir(self.pathen):
            if os.path.splitext(i)[1] == '.zip':
                with zipfile.ZipFile(self.pathen + "/{0}".format(i)) as self.myzip:
                    with self.myzip.open(self.pathE) as self.myfile:
                        with open("./{0}".format(self.pathE), 'wb') as self.xfil:
                            self.xfil.write(self.myfile.read())

    def works(self):
        self.wr_file = xlrd.open_workbook("./{0}".format(self.pathE))
        self.sheet = self.wr_file.sheet_by_index(0)
        self.rownum = self.sheet.nrows
        self.colnum = self.sheet.ncols
        if self.rownum > 0 and self.colnum > 0:
            self.f = open(self.pathv, 'w', encoding="utf-8")
            for raw in range(self.rownum):
                self.strs = " "
                for cal in range(self.colnum):
                    self.strs = self.strs + str(self.sheet.row(raw)[cal]).replace("text:", " ").replace("'",
                                                                                                        "").replace(",",
                                                                                                                    "").replace(
                        "empty", "").replace("number", "")
                    if cal + 1 == self.colnum:
                        self.f.write(self.strs + "\n")
            else:
                pass
            self.f.close()
        else:
            sys.exit(1)
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
        print("\033[1;37;40mЗнайдено", end='')
        print("\033[1;36;40m {0} ".format(len(self.results)), end="")
        print("\033[1;37;40mспівпадінь")
        for i in self.results:
            print("\033[1;34;40m-------------------------------------")
            self.textsa = str(self.textv[i - 23: i - 4])
            self.numer = str(self.textv[i - 2: i + 9])
            self.textse = str(self.textv[i + 12: i + 58]).replace(":", " ")
            print("\033[1;37;40m{0}".format(self.textsa), end=""'')
            print("\033[1;36;40m {0}".format(self.numer), end="")
            print("\033[1;37;40m {0}".format(self.textse), )
        os.remove(self.pathv)
        print("\033[1;30;40m ")


if __name__ == '__main__':
    print("\033[1;33;40mОбробка даних!")
    m = Main()
    m.works()
    m.worck()
