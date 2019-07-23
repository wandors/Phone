# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os

paths = "D://tel.txt"
paths1 = "D://Витрати.txt"
ff = open(paths, 'r')
tetx = ff.read()
ff.close()
text1 = tetx.replace('-', '')
text2 = text1.replace(')', '')
text3 = text2.replace('\n', '')
text4 = text3.replace(' ', '')
text5 = text4.replace(' ', '')
text6 = text5.replace('(', '\n')
text7 = text6.replace('0988204750', '\n0988204750')
fff = open('D://telss.txt', 'w')
fff.write(text7)
fff.close()
print(text7)
