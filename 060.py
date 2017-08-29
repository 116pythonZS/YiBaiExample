#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：计算字符串长度。　
"""


def main():
    text = "这是一个中文字符串"
    text2 = "this is not chinese!"
    print("中文长度'%s':%d"%(text,len(text)))
    print("非中文长度'%s':%d"%(text2,len(text2)))


if __name__ == "__main__":
    main()

 