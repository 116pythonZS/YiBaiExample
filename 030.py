#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""

import math
def check(num):
    result = 1
    if num < 10000 or num > 100000:
        print("<%d>不是一个5位数"%(num,))
        result = -1
    else:
        for idx in range(1,3):
            left = (num // math.pow(10,5-idx)) % math.pow(10,idx-1)
            if idx == 1:
                left = num // math.pow(10,5-idx)
            right = num % math.pow(10,idx) // math.pow(10,idx-1)
            if left != right:
                result = 0
                break

    return result


def main():
    prompt = "继续(Y)or退出(N):"
    choice = input(prompt)
    while "n" != choice and "N" != choice:
        text = int(input("输入一个5位数:"))
        result = check(text)
        if result == 0:
            print("%d 不是回文数"%(text,))
        elif result == 1:
            print("%d 是回文数"%(text,))

        choice = input(prompt)


if __name__ == "__main__":
    main()

 