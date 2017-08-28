#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：按相反的顺序输出列表的值。
"""

def resverList(l):
    relist = l[::-1]
    return relist


def main():
    li = [1,2,3,4,5,6]
    relist = resverList(li)
    print("原始列表:", li)
    print("反序列表:", relist)


if __name__ == "__main__":
    main()

 