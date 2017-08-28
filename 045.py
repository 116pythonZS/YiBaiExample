#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：统计 1 到 100 之和。
"""

def calc(maxnum):
    result = 0
    for i in range(1,maxnum+1):
        result += i
    return result

def main():
    print(calc(100))


if __name__ == "__main__":
    main()

 