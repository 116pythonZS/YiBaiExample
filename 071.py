#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
题目：编写input()和output()函数输入，输出5个学生的数据记录。
"""

stuList = []
def input_stu():
    for idx in range(0, 3):
        stu = {"name": input("输入名字:"), "score": input("输入分数:")}
        stuList.append(stu)

def output_stu():
    for idx in range(0, len(stuList)):
        print("第%d个学生信息:{名字:%s  分数:%s}"%((idx+1), stuList[idx]["name"],stuList[idx]["score"]))

def main():
    input_stu()
    output_stu()


if __name__ == "__main__":
    main()

 