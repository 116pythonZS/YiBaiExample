#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/21.

"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

def test(maxTimes):
    inputs = []
    src = []
    for i in range(0, maxTimes):
        item = int(input("请输入整数:"))
        src.append(item)
        inputs.append(item)

    inputs.sort()
    print("原始数据:", src)
    print("排序数据:", inputs)

test(3)