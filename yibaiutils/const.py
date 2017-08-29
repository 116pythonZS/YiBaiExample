#!/usr/bin/python 
# -*- coding=utf8 -*-
# Created by carrot on 2017/8/29.

"""
定义常量
"""

class _const:
    class ConstError(TypeError) : pass

    DIC = {}
    
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("constant reassignment error!")
        self.__dict__[key] = value

import sys

sys.modules[__name__] = _const()

 