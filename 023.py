#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

"""
输出一下类型的图案
   *
  ***
 *****
*******
 *****
  ***
   *
"""
from yibaiutils import ybutils
@ybutils.deco
def show(num):
    total = num+1
    for i in range(1,total):
        key = i
        if i > int(total/2):
            key = total - i
        leftspace = " " * (int(total/2)-key)
        leftstar = "*"*key
        rightstar = "*"*(key-1)
        rightspace = " "*(int(total/2) -key-1)
        line = leftspace+leftstar+rightstar+rightspace
        print(line)

def main():
    num = int(input("请输入一个奇数>> "))
    show(num)

if __name__ == '__main__':
    main()

 