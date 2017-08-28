#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""

from yibaiutils import ybutils

@ybutils.deco
def calc(num):
    fz = 2
    fm = 1
    value = 0
    for idx in range(1, num+1):
        value += fz / fm
        fm , fz = fz, fz+fm
    print(value)

def main():
    num = int(input("输入项数:"))
    calc(num)

if __name__ == '__main__':
    main()