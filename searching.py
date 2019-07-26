# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os

patht = "./telss.txt"
pathv = "./Vitr1.txt"
listel = []

ff = open(pathv, 'r')
textv = ff.read()
ff.close()

ff = open(patht, 'r')
textt = ff.readlines()
ff.close()
for i in textt:
    listel.append(i.replace('\n', ''))

print(listel)
for trl in listel:
    reults = textv.find(trl)
    if reults == -1:
        pass
    else:
        print(trl)
