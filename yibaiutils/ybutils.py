#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/27.

import time
def deco(func):
    def _deco(*args, **kwargs):
        startT = time.time()
        ret = func(*args, **kwargs)
        endT = time.time()
        print("耗时:%f" % (endT - startT,))
        return ret
    return _deco

 