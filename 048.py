#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：数字比较。
"""


def main():
    i = 10
    j = 20
    if i > j:
        print('%d 大于 %d' % (i,j))
    elif i == j:
        print('%d 等于 %d' % (i,j))
    elif i < j:
        print('%d 小于 %d' % (i,j))
    else:
        print('未知')


if __name__ == "__main__":
    main()

 