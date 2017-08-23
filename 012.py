#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/23.

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

import math

def isPrime(num):
    result = True
    if num <= 1:
        print("不是素数:%d" %(num,))
        return False
    sqrtValue = int(math.sqrt(num))
    for idx in  range(2,sqrtValue + 1):
        if num % idx == 0:
            result = False
            break
    return result

def main():
    primeNum = []
    for idx in range(101,201):
        if isPrime(idx):
            primeNum.append(idx)
    print("101-200之间的素数 总共%d个:" % (len(primeNum),))
    for idx in range(len(primeNum)):
        print(primeNum[idx])

if __name__ == '__main__':
    main()
 