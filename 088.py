#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
"""


def main():
    n = 7
    while n > 0:
        num = int(input("输入一个整数"))
        if (num <1) or (num > 50): continue
        n -= 1
        print("*"*num)


if __name__ == "__main__":
    main()

 