#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
"""

import time

def main():
    """
    暂停1秒输出
    """
    print("启动:%f" %(time.time(),))
    time.sleep(1)
    print("暂停1秒之后:%f" % (time.time(),))
    
if __name__ == '__main__':
    main()
    