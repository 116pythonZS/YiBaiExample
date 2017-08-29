#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""

import random

def createList(num):
    li = []
    for idx in range(0, num):
        li.append(random.randint(1,100))
    return li

def calc(l):
    if not l:
        print("列表不能为空")
    maxi = 0
    mini = len(l)-1
    for i in range(0,len(l)):
        if l[i] < l[mini]:
            mini = i
        if l[i] > l[maxi]:
            maxi = i
    l[0], l[maxi] = l[maxi],l[0]
    l[len(l)-1], l[mini] = l[mini], l[len(l)-1]
    
def main():
    l = createList(10)
    print("交换前:", l)
    calc(l)
    print("交换后:",l)


if __name__ == "__main__":
    main()

 