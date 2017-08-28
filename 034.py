#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：练习函数调用。
"""

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()

def main():
    three_hellos()


if __name__ == "__main__":
    main()

 