#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/26.


"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
"""

import math

def creatList(num, count=5):
    datas = []
    for idx in range(count):
        data = int(num * math.pow(10, idx))
        if len(datas):
            data = data + datas[idx - 1]
        datas.append(data)
    return datas

def main() :
    num = int(input("输入数子:"))
    count = int(input("数位位数"))
    datas = creatList(num, count)
    print(datas)
    print(sum(datas))


if __name__ == '__main__':
    main()

 