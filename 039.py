#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""

from yibaiutils import ybutils

@ybutils.deco
def buildIn(l, num):
    li = l.copy()
    li.append(num)
    li.sort()
    print("build_in:", li)

@ybutils.deco
def custom(l, num):
    # li.append(num)
    li = l.copy()
    for idx in range(0,len(li)):
        if li[idx]>num:
            li.insert(idx,num)
            break
    print("custom:",li)

def main():
    li = [1,3,5,7,9,11,45,67,89,123,435,1235]
    num = 863
    buildIn(li,num)
    custom(li, num)


if __name__ == "__main__":
    main()

 