#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/23.


"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""

import math

def isNarcissusNum(num):
    if num < 100 or num > 1000:
        return False
    left = num // 100
    mid = num // 10 % 10
    right = num % 10
    return num == math.pow(left,3) + math.pow(mid,3) + math.pow(right,3)

def main():
    narcissusNums = []
    for idx in range(100,1000):
        if isNarcissusNum(idx):
            narcissusNums.append(idx)

    print("水仙花数总共%d个:" % (len(narcissusNums),))
    for idx in range(len(narcissusNums)):
        print(narcissusNums[idx])

if __name__ == '__main__':
    main()


 