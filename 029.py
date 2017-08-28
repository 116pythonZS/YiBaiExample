#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

import math

def calc(num):
    result =  [0, []]
    if num <= 0:
        print("%d不是正整数"%(num,))
        return None
    else:
        n = num
        idx = 0
        while num // 10 > 0:
            result[0] += 1
            value = str(int(num % 10))
            result[1].append(value)
            num = num // 10
        else:
            result[0] += 1
            value = str(int(num % 10))
            result[1].append(value)
        return result

def main():
    num = int(input("输入一个正整数:"))
    result = calc(num)
    if not result:
        print("不是一个正整数")
    else:
        print("是%d位数  倒置为%s"%(result[0],"".join(result[1])))


if __name__ == "__main__":
    main()

 