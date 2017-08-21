#!/usr/bin/python
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/21.


"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""

def fib1(n):
    a, b = 1, 1
    for i in  range(1, n-1):
        a, b = b, a+b
    return b

def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n-1) + fib2(n-2)

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


nValue = int(input("输入整数:"))
print(fib1(nValue))
print(fib2(nValue))
print(fib(nValue))