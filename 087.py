#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：结构体作为参数
"""

class student:
    x = 0
    c = 0

def f(stu):
    stu.x = 20
    stu.c = 'c'


def main():
    a= student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x,a.c)


if __name__ == "__main__":
    main()

 