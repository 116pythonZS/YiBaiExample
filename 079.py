#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：字符串排序。
"""


def main():
    li = []
    for idx in range(0,3):
        text = input("输入一个字符串:")
        li.append(text)

    print("原始字符串:"," ".join(x for x in li))
    li.sort()
    print("排序字符串:"," ".join(x for x in li))


if __name__ == "__main__":
    main()

 