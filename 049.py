#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：使用lambda来创建匿名函数。
"""

MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

def main():
    a ,b = 10,20
    print("(%d,%d)最大值是:%d"%(a, b, MAXIMUM(a,b)))
    print("(%d,%d)最小值是:%d"%(a, b, MINIMUM(a,b)))


if __name__ == "__main__":
    main()

 