#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：输入3个数a,b,c，按大小顺序输出。
"""


def main():
    num1 = int(input("输入第一个数字:"))
    num2 = int(input("输入第二个数字:"))
    num3 = int(input("输入第三个数字:"))

    li = [num1, num2, num3]
    li.sort()
    print("排序后的数据:",li)


if __name__ == "__main__":
    main()

 