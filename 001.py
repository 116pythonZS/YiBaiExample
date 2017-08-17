#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @version: 1.0
    @author : Carrot
    @time   : 2017/8/17 18:25
"""

src = [1, 2, 3, 4, 5]
result = []
for i in src:
	for j in src:
		for k in src:
			if (i != j) and (j != k) and (i != k):
				result.append(i * 100 + j * 10 + k)

print("数据总数:%d", len(result))
for item in result:
	print(item)
	