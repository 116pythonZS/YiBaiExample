#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/30.

"""
 题目：字符串日期转换为易读的日期格式。
"""

from dateutil import parser

def main():
    dt = parser.parse("Aug 30 2017 12:00AM")
    print (dt)


if __name__ == "__main__":
    main()

 