#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/30.

"""
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""


def main():
    # f1 = open("f1","w+")
    # f1.write("abcxyz")
    # f1.close()
    # 
    # f2 = open("f2","w+")
    # f2.write("efguvw")
    # f2.close()

    f1 = open("f1","r")
    f2 = open("f2","r")
    text1 = f1.read()
    text2 = f2.read()
    f1.close()
    f2.close()
    text = text1 + text2

    f3 = open("f3","w+")
    text = "".join(x for x in sorted(text))
    print(text)

    f3.write(text)
    f3.close()


if __name__ == "__main__":
    main()

 