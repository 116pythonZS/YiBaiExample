#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/26.

"""
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""

def main():
    start = 1
    datas={}
    for idx in range(10,0,-1):
        if  idx == 10:
            datas[idx] = 1
        else:
            datas[idx] = (datas[idx+1]+1)*2
    print(datas)


if __name__ == '__main__':
    main()

 