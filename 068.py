#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
"""

import random
def createList(num):
    li = []
    for idx in range(0, num):
        li.append(random.randint(1,100))
    return li

def move(l,m):
    left = l[0:m]
    for idx in range(0, m):
        l.insert(idx, left[idx])
    right = l[len(l)-m:len(l)]
    for idx in range(0,m):
        item = right[idx]
        l.remove(item)
        l[idx] = item

def main():
    li = createList(12)
    print("移动前id=%d"%(id(id),),"value=",li)
    move(li, 5)
    print("移动后id=%d"%(id(id),),"value=",li)


if __name__ == "__main__":
    main()

 