# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os


class Main:
    patht = "./telss.txt"
    pathv = "./us.txt"
    listel = []
    imters = []
    def __init__(self):
        self.ff = open(self.pathv, mode="r", encoding="utf-8")
        self.textv = self.ff.read().replace("\n", ' ')
        self.ff.close()
        self.texts = self.textv
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
                self.imters = []
                pass
            else:
                self.tels(telep=self.trl, text=self.textv, result=self.result)

    def tels(self, telep, text, result):
        result += 1
        self.textv = text[result:]
        self.imters.append(result)
        self.result = self.textv.find(telep)
        if self.result == -1:
            self.findal()
        else:
            self.tels(telep=telep, text=self.textv, result=self.result)
    def findal(self):
        self.x = 1
        for i in self.imters:
            self.x = self.x + i
            print( self.texts[self.x - 22: self.x + 58])
            print("-----------------")
        return  self.x








if __name__ == '__main__':
    m = Main()
    m.worck()
