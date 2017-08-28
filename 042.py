#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
 题目：学习使用auto定义变量的用法。
"""

num=2
def autofunc():
    num = 1
    print( 'internal block num = %d' % num)
    num += 1

def main():
    global num
    for i in range(3):
        print ('The num = %d' % num)
        num += 1
        autofunc()


if __name__ == "__main__":
    main()

 