#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/24.

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
"""
class stringParase(object):
    @classmethod
    def parase(cls, words):
        datas = {"字母":0, "空格":0, "数字":0, "其他":0}
        for c in words:
            if c.isalpha():
                datas["字母"] += 1
            elif c.isdigit():
                datas["数字"] += 1
            elif c.isspace():
                datas["空格"] += 1
            else:
                datas["其他"] + 1
        return datas




def main():
    words = input("输入:")
    datas = stringParase.parase(words)
    for k, v in datas.items():
        print("%s = %d" % (k, v))

if __name__ == '__main__':
    main()
 