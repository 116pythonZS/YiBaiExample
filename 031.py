#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/28.

"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
weekDict = {"Monday":"星期一","Tuesday":"星期二","Wednesday":"星期三","Thursday":"星期四","Friday":"星期五","Saturday":"星期六","Sunday":"星期日"}

def getResult(s):
    if not s :
        return None
    keys =  weekDict.keys()

    result = []
    query = s.lower()
    for key in keys:
        value = key.lower()
        if value.startswith(query):
        # if query == value[0:len(query)]:
            result.append(key)
    return result


def main():
    find = False
    text = ""
    prompt = "请输入一个字母"
    count = 0
    while not find:
        text += input(prompt)
        result = getResult(text)
        count += 1
        if not result:
            pass
        else:
            if len(result) > 1:
                prompt = "请输入下一个字母"
            else:
                print("查到的结果%s : %s"%(result[0], weekDict[result[0]]))
                find = True
                text = ""
        if count > 3:
            text = ""
            prompt = "应该出错了, 重新输入一个字母"


if __name__ == "__main__":
    main()

 