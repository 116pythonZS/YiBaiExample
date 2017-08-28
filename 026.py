#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

"""
题目：利用递归方法求5!。
"""
from yibaiutils import ybutils
def recursive(num):
    if num == 1:
        return 1
    else:
        return num*recursive(num-1)

@ybutils.deco
def main():
    num = int(input("输入一个整数:"))
    print(recursive(num))

if __name__ == '__main__':
    main()