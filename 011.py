#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/23.

"""
题目：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""

import time


rabbits = []

def recursive(month):
    if month == 1 or month == 2:
        return 1
    return recursive(month - 1) + recursive(month - 2)

def testRecursive(month):
    global rabbits
    rabbits = []
    for index in range(1, month+1):
        rabbits.append(recursive(index))

def normalFun(month):
    global  rabbits
    rabbits = [1,1]
    # rabbits.append(1)
    # rabbits.append(1)
    for index in range(2,month):
        f1 = rabbits[index-2]
        f2 = rabbits[index-1]
        rabbits.append(f1+f2)

def outputRabbits():
    for rabbit in range(0,len(rabbits)):
        print("第%d个月,兔子数:%lu" %(rabbit+1, rabbits[rabbit]))

def test(funcName, param):
    start = time.time()
    funcName(param)
    end = time.time()
    print("%s: 月数:%d 耗时:%f" % (funcName.NAME, param, end - start))

def setup():
    normalFun.NAME = "普通方法"
    testRecursive.NAME = "递归方法"
def main():
    maxMonth = int(input("输入月数:"))
    for month in range(1,maxMonth+1):
        test(normalFun, month)
        test(testRecursive, month)

if __name__ == '__main__':
    setup()
    main()
 