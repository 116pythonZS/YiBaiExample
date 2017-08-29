#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：八进制转换为十进制
"""


def main():
    n = 0
    p = input('输入一个八进制数字:')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)


if __name__ == "__main__":
    main()

 