#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/30.

"""
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
"""


def main():
    text = input("输入:")
    uppperText = text.upper()
    fp = open("test","w+")
    fp.write(uppperText)
    fp.close()


if __name__ == "__main__":
    main()

 