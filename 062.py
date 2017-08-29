#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：打印出杨辉三角形（要求打印出10行如下图）。
"""

def yhTriangle(num):
    result = []
    for idx in range(0,num):
        if idx == 0:
            result.append([1])
            continue
        line = []
        for k in range(0,idx+1):
            preline = result[idx-1]
            prelineitem1 = 0
            if k-1 >= 0:
                prelineitem1 = preline[k-1]
            prelineitem2 = 0
            if k < len(preline):
                prelineitem2 = preline[k]
            line.append(prelineitem1 +prelineitem2)

        result.append(line)
    return result

def main():
    print("\n".join([str(x) for x in yhTriangle(10)]))


if __name__ == "__main__":
    main()

 