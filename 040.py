#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
将一个数组逆序输出。
"""

def resverArry(l):
    li = l.copy()
    count = len(li)
    for idx in range(0, count//2):
        li[idx], li[count - idx-1] = li[count-idx-1], li[idx]
    return li

def main():
    li = [4,5,6,7,8,9]
    reli = resverArry(li)
    print("原始数组:",li)
    print("逆序数组,",reli)


if __name__ == "__main__":
    main()

 