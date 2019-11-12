# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os
import re
import mmap

patht = "./telss.txt"
pathv = "./us.txt"
listel = []

ff = open(pathv,  mode="r", encoding="utf-8")
textv = ff.read()
ff.close()
textv = textv.replace(" ", "")

ff = open(patht, 'r')
textt = ff.readlines()
ff.close()
for i in textt:
    listel.append(i.replace('\n', ''))
results = 0
for trl in listel:
    myb = trl.encode('utf-8')
    f = open(pathv, 'r+b')
    mf = mmap.mmap(f.fileno(), 0)
    mf.seek(0)  # reset file cursor
    m = re.search(myb, mf)
    print(m.start(), m.end())
    mf.close()
    f.close()

print("Обробка закінчена!!!")
