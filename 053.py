#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：学习使用按位异或 ^ 。
"""


def main():
    a = 0o77
    b = a ^ 3
    print('a ^ b = %d' % b )
    b ^= 7
    print('a ^ b = %d' % b)


if __name__ == "__main__":
    main()

 