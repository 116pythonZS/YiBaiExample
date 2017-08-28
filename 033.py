#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
按逗号分隔列表
"""


def main():
    li = ['1','b',2,"abd"]
    print(",".join(str(value) for value in li))


if __name__ == "__main__":
    main()

 