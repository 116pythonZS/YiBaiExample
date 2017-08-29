#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
"""


def main():
    value = 0
    for idx in range(10, 100):
        if (809*idx < 10000) and  (8 * idx < 100) and (9 * idx >= 100) and (809*idx == 800*idx +9*idx):
            value = idx
            break
    print ("809*%d = 800*%d + 9*%d"%(value, value, value))



if __name__ == "__main__":
    main()

 