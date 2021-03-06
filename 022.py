#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/26.

"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
from yibaiutils import ybutils

class team(object):
    def __init__(self, name):
        self.name = name
        self.ignoreTeams = None
        self.vsTeam = None

    def setIgnoreTeam(self, teams):
        self.ignoreTeams = teams

    def setVSTeam(self,vsteam):
        self.vsTeam = vsteam

@ybutils.deco
def main():
    for a in ['x', 'y', 'z']:
        for b in ['x', 'y', 'z']:
            if a == b:
                continue
            for c in ['x', 'y', 'z']:
                if (a != b) and (b != c) and (c != a) and (a != 'x') and (c != 'x') and (c != 'z'):
                    print('a和%s比赛，b和%s比赛，c和%s比赛' % (a, b, c))

if __name__ == '__main__':
    main()
 