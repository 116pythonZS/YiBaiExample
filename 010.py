#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
"""

import time

def main():
    print ("开始时间:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),))
    time.sleep(1)
    print ("结束时间:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),))

if __name__ == '__main__':
    main()