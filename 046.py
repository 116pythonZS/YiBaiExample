#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
"""

def main():
    num = int(input("輸入一個數:"))
    while num**2 > 50:
        num = int(input("輸入一個數:"))


if __name__ == "__main__":
    main()

 