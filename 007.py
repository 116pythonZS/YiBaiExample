#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/21.

"""
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
"""

import  copy

l = [[3,4,5], 2, "nihao"]
l2 = l[:]
print("l[0]:",id(l[0]))
print("l2[0]",id(l2[0]))

l3 = l.copy()
print("l[0]:",id(l[0]))
print("l3[0]",id(l3[0]))


l4 = copy.copy(l)
print("l[0]:",id(l[0]))
print("l4[0]",id(l4[0]))


l5 = copy.deepcopy(l)
print("l[0]:",id(l[0]))
print("l5[0]",id(l5[0]))
