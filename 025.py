#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

"""
题目：求1+2!+3!+...+20!的和。
"""

from yibaiutils import ybutils

def normal(num):
    value = 1
    for idx in range(1, num+1):
        value *= idx
    return value

def recursive(num):
    if num == 1:
        return 1
    else:
        return num*recursive(num-1)

@ybutils.deco
def calcNormal(num):
    value = 0
    for idx in range(1, num+1):
        value += normal(idx)
    print(value)

@ybutils.deco
def calcRecursive(num):
    value = 0
    for idx in range(1, num+1):
        value += recursive(idx)
    print(value)


def main():
    num = int(input("亲输入一个正整数:"))
    print("普通方法->")
    calcNormal(num)
    print("递归方法->")
    calcRecursive(num)

if __name__ == '__main__':
    main()