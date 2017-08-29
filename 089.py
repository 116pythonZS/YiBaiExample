#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
"""


def main():
    srcNum = input("输入一个4位数:")
    dest = []
    for idx in range(len(srcNum)):
        dest.append(int(srcNum[idx]) + 5 % 10)
    dest[0], dest[3] = dest[3], dest[0]
    dest[1], dest[2] = dest[2], dest[1]

    print("".join(str(x) for x in dest))


if __name__ == "__main__":
    main()

 