#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
"""

def calc(l):
    src = l.copy()
    start = 0
    while len(src)>1:
        rlist = []
        for i in range(0, len(src)):
            if (start+i+1)!=0 and (start+i+1) %3 ==0:
                rlist.append(src[i])
        start = (len(src)+start)%3
        for obj in rlist:
            src.remove(obj)
        srcstr = " ".join(str(item) for item in src)
        rlstr = " ".join(str(index) for index in rlist)
        print("start=",start," src = ", srcstr, "   rlist = ", rlist)

    return src

def main():
    n = 34
    li = []
    for i in range(0, n):
        li.append(i+1)

    print(li)
    result = calc(li)
    print(result[0])



if __name__ == "__main__":
    main()

