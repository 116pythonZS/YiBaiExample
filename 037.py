#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
"""

def sortList(l):
    li = l.copy()
    for i in range(0, len(li)):
        for j in range(i, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j],li[i]
    return li

import random
def main():
    li = []
    for idx in range(1, 11):
        li.append(random.randint(1,1000))
    reli = sortList(li)
    print("原始数据:",li)
    print("排序数据:",reli)


if __name__ == "__main__":
    main()

 