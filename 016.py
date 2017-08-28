#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/24.

"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""

import time
import datetime

def testTime():
    print(time.time())  # 1498539133.655
    print(time.localtime())  # tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1, tm_yday=178, tm_isdst=0
    print(time.asctime())  # 'Tue Jun 27 12:53:50 2017'
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))  # '2017-06-27 13:00:57'

def testDatetime():
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
    pass


def main():
    testTime()
    testDatetime()

if __name__ == '__main__':
    main()

 