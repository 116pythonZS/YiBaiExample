#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
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

def print3Matrix(matrix):
    for line in matrix:
        print(" ".join("%4d"%(n,) for n in line))

def add3Matrix(x,y):
    result = []
    for i in range(0,len(x)):
        line = x[i]
        sumline = []
        for j in range(0, len(line)):
            sumline.append(x[i][j] + y[i][j])
        result.append(sumline)
    return result
        
def main():
    X = create3Matrix()
    print3Matrix(X)
    print("+")
    Y = create3Matrix()
    print3Matrix(Y)
    print("=")
    result = add3Matrix(X,Y)
    print3Matrix(result)

if __name__ == "__main__":
    main()

 