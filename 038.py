#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""

import random
def create3Matrix():
    matrix=[]
    for i in range(0,3):
        li= []
        for j in range(0,3):
            li.append(random.randint(1,1000))
        matrix.append(li)
    return matrix

def main():
    matrix = create3Matrix()
    for line in matrix:
        print(" ".join("%4d"%(n,) for n in line))

    total = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j:
                total += matrix[i][j]
    print("对角线之和:%d" %(total,))


if __name__ == "__main__":
    main()

 