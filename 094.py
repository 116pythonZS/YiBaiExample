#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
"""

import time
import random

def main():
    play_it = input("想要继续玩吗('y'or'n')")
    while play_it == 'y':
        i = random.randint(0,2**32) % 100
        start = time.clock()
        # a = time.time()
        guess = int(input('输入你的猜测:'))
        while guess != i:
            if guess > i:
                guess = int(input('太小了, 输入你的猜测:'))
            else:
                guess = int(input('太大了, 输入你的猜测:'))
        end = time.clock()
        # b = time.time()
        # var = (end - start) / 18.2
        # print( var)
        # if var < 15:
        #     print('超赞')
        # elif var < 25:
        #     print('路人甲')
        # else:
        #     print('二师兄的智商')
        print('恭喜:谜底是%d 耗时:%f'%(i,end-start))
        play_it = input('是否继续?')


if __name__ == "__main__":
    main()

 