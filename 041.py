#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：模仿静态变量的用法。
"""

class test_static(object):
    staticvar = []

    def append(self,obj):
        self.staticvar.append(obj)



def main():
    a = test_static().staticvar
    b = test_static().staticvar
    c = test_static().staticvar

    o = test_static()

    a.append(1)
    b.append(2)
    c.append(3)
    o.append(4)

    print("a:",a)
    print("a:",b)
    print("a:",c)
    print("o.staticvar:",o.staticvar)

    print(id(a))
    print(id(b))
    print(id(c))
    print(id(o.staticvar))



if __name__ == "__main__":
    main()

 