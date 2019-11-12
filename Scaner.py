# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os


class Main:
    patht = "./telss.txt"
    pathv = "./us.txt"
    listel = []
    imters = 0
    def __init__(self):
        self.ff = open(self.pathv, mode="r", encoding="utf-8")
        self.textv = self.ff.read()
        self.ff.close()
        #self.textv = self.textv.replace(" ", "")
        self.ff = open(self.patht, 'r')
        self.textt = self.ff.readlines()
        self.ff.close()
    def worck(self):
        self.results = 0
        self.text = len(self.textv)
        for i in self.textt:
            self.listel.append(i.replace('\n', ''))
        for self.trl in self.listel:
            self.result = self.textv.find(self.trl)
            if self.result == -1:
                pass
            else:

                self.tels(telep=self.trl, text=self.textv, result=self.result,inter= i)

    def tels(self, telep, text, result):

        result += 1
        self.textv = text[result:]
        print(result-1)
        print(result+55)
        print(self.textv[:55].replace('\n', ' '))

        self.result = self.textv.find(telep)
        if self.result == -1:
            pass
        else:
            self.tels(telep=telep, text=self.textv,result=self.result)








if __name__ == '__main__':
    m = Main()
    m.worck()
