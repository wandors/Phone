# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os

pathc = "D://00001.vcf"
ff = open(pathc, 'r')
tint = ff.readlines()
ff.close()
tel = []
for i in tint:
    fi = i.find("TEL")
    if fi == 0:
        tel.append(i.replace("\n", ''))

tels = tel
telss = []
for i in tels:
    ii = i.replace('TEL;TYPE=CELL:', '')
    ii = ii .replace("TEL;TYPE=CELL;TYPE=PREF:", '')
    ii = ii.replace("TEL;TYPE=WORK:", '')
    ii = ii.replace("TEL;TYPE=PREF:", '')
    ii = ii.replace("TEL;TYPE=VOICE:", '')
    ii = ii.replace("TEL;TYPE=car:", '')
    ii = ii.replace("-", '')
    ii = ii.replace("+", '')

    if len(ii) == 10:
        telss.append('38' + ii)
    if len(ii) == 12:
        telss.append(ii)
pathv = "D://Vitr.txt"
ff = open(pathv, 'r')
textv = ff.read()
ff.close()
for trl in telss:
    reults = textv.find(trl)
    if reults == -1:
        pass
    else:
        print(trl)


