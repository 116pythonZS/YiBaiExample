#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：创建一个链表。
"""

from yibaiutils import const

const.NAME = "序号"
const.NEXT = "下一个节点"

Head = {const.NAME:"0",const.NEXT:None}
current = Head
def createList():
    global current
    text = input("请输入序号:")
    while text != ".":
        node = {const.NAME:text,const.NEXT:None}
        current[const.NEXT] = node
        current = node
        text = input("请输入序号:")

def printList():
    node = Head
    while node:
        print("节点值:%s"%(node[const.NAME],))
        node = node[const.NEXT]

def main():
    createList()
    printList()


if __name__ == "__main__":
    main()

 