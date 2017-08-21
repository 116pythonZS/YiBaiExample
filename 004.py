#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/21.

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

def isLeapYear(y):
    return (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))

monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def checkDate(y, m, d):
    if m <= 0 or m > 12:
        print("请输入正确的月份")
        return False

    leapYear = isLeapYear(y)
    md = monthDays[m]
    if leapYear and m == 2:
        md += 1
    if d <= 0 or d > md:
        print("请输入正确的日")
        return False
    return True

def getDaysMonth(y, m, d):
    if checkDate(y, m, d):
        days = 0
        for idx in range(0,m):
            days += monthDays[idx]
        if m > 2 and isLeapYear(y):
            days += 1

        days += d
        return days
    else:
        return None

for i in  range(1,10):
    year = int(input("输入年:"))
    month = int(input("输入月:"))
    day = int(input("输入日:"))
    value = getDaysMonth(year, month, day)
    if value:
        print(value)
