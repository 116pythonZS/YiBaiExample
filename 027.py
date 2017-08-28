#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""

def resver(text):
    textLen = len(text)
    if textLen == 1:
        return text
    else:
        return text[-1] + resver(text[:-1])

def main():
    text = input("输入:")
    print(resver(text))

if __name__ == '__main__':
    main()