#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：反向输出一个链表。
"""


def main():
    li = []
    text = input("请输入数据:")
    while text != ".":
        li.append(text)
        text = input("请输入数据:")
    print("正序输出:", li)
    li.reverse()
    print("倒序输出:", li)


if __name__ == "__main__":
    main()

 