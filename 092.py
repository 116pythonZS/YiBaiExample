#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：时间函数举例2。
"""

import time

def main():
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()

    print(end - start)


if __name__ == "__main__":
    main()

 