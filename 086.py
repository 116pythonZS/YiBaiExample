#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数。
"""


def main():
    num = int(input("输入一个整数:"))
    count = 1
    while int(str("9"*count))%num != 0:
        count +=1

    minNum = int(str("9"*count))
    print("最少%d个9 才能整除%d %d = %d * %d"%(count, num,minNum,num,int(minNum/num)))


if __name__ == "__main__":
    main()

 