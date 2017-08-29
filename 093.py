#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：时间函数举例3。
"""

import time

def main():
    start = time.clock()
    for i in range(10000):
        print(i)
    end = time.clock()
    print('different is %6.3f' % (end - start) )


if __name__ == "__main__":
    main()

 