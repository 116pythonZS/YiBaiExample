#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：求100之内的素数。
"""
def isPrimeNum(num):
    result = True
    if num <= 1:
        result = False
    for idx in range(2, num):
        if num % idx == 0:
            result = False
            break
    return result

def primes(minnum, maxnum):
    result = []
    for idx in range(minnum, maxnum+1):
        if isPrimeNum(idx):
            result.append(idx)

    return result

def main():
    minnum = int(input("输入最小整数"))
    maxnum = int(input("输入最大整数"))
    print(",".join(str(n) for n in primes(minnum, maxnum)))


if __name__ == "__main__":
    main()

 