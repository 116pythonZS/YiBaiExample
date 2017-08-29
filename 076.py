#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""

# 奇数
def calcOdd(num):
    result = 1.0
    for idx in range (1,num+1,2):
        result += 1 / idx
    return result

# 偶数
def calcEven(num):
    result = 0
    for idx in range (2,num+1,2):
        result += 1 / idx
    return result
    

def calc(num):
    result = 0
    if num % 2 == 0:
        result = calcEven(num)
    else:
        result = calcOdd(num)

    return result

def main():
    num = int(input("输入一个数字:"))
    print(calc(num))



if __name__ == "__main__":
    main()

 