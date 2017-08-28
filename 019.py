#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/26.

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

def reduceNum(num):
    members = []
    for idx in range(1,num):
        if  num % idx == 0:
            members.append(idx)
    return members

def main():
    counts = {}
    for idx in range(2,1001):
        result = reduceNum(idx)
        if result and idx == sum(result):
            counts[idx]=result
    print("完数个数:%d" % (len(counts),))
    print(counts)
    for k, v in counts.items():
        print("%s = %s" % (k,v))
    print("{}".format(counts.items()))


if __name__ == '__main__':
    main()