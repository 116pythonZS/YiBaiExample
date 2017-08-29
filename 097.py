#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/30.

"""
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
"""


def main():
    filename = input('输入文件名:')
    fp = open(filename,"w")
    ch = input('输入字符串:')
    while ch != '#':
        fp.write(ch)
        ch = input('')
    fp.close()


if __name__ == "__main__":
    main()

 