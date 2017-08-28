#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：学习使用按位取反~。
"""


def main():
    a = 234
    b = ~a
    print('The a\'s 1 complement is %d' % b)
    a = ~a
    print('The a\'s 2 complement is %d' % a)


if __name__ == "__main__":
    main()

 