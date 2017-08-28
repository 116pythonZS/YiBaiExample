#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：两个变量值互换。
"""

def swap(x,y):
    print("swap:交換前x=%d y=%d"%(x,y))
    x,y = y,x
    print("swap:交換后x=%d y=%d"%(x,y))

def main():
    x ,y = 10,20
    print("main:交換前x=%d y=%d"%(x,y))
    swap(x,y)
    print("main:交換后x=%d y=%d"%(x,y))



if __name__ == "__main__":
    main()

 