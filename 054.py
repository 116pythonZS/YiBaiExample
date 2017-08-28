#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：取一个整数a八进制从右端开始的4〜7位。
"""


def main():
    num = 9
    num1 = num>>4
    num2 = 7
    print("%o\t%o"%(num,num1&num2))


if __name__ == "__main__":
    main()

 