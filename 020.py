#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/26.


"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
程序分析：无
"""

def jumpHeight(start, num):
    height= start
    datas = {0:height}
    for idx in range(1, num +1):
        height = height / 2
        datas[idx] = height
        datas[0] += 2*datas[idx]

    return datas

def main():
    start = 100
    num= 10
    result = jumpHeight(start,num)
    print (result)
    print("第10次着地%f",result[0] - 2* result[num])
    print("第10次反弹%f",result[num])



if __name__ == '__main__':
    main()