# -*- coding: utf-8 -*-
__author__ = 'Сергей Полунец'
import sys
import os


class Main:
    def __init__(self):
        print(os.listdir("."))
        print(os.path.exists("./test.py"))


if __name__ == '__main__':
    m = Main()