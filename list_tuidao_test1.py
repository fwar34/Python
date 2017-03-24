#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: list_tuidao_test1.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 09:59:57 AM CST
# Content: 列表的推导式

v1 = [1, 3, 5]
v2 = [2, 4, 6]
print(v1)
print(v2)

v3 = [x * y for x in v1 for y in v2]
print(v3)

v4 = [v1[i] * v2[i] for i in range(len(v1))]
print(v4)

v5 = [x * 3 for x in v2 if x > 2]
print(v5)

#列表推导式可以使用复杂的表达式或者嵌套函数
v6 = [str(round(355/113, i)) for i in range(1, 6)]
print(v6)


#python的列表还可以嵌套
#3 * 4矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#以下将3X4的矩阵列表转换为4X3列表
v7 = [[row[i] for row in matrix] for i in range(4)]
print(v7)

#也可以使用以下方法来实现
v8 = []
for i in range(4):
    v8.append([row[i] for row in matrix])

print(v8)

#另外一种实现方法
v9 = []
for i in range(4):
    vtemp = []
    for row in matrix:
        vtemp.append(row[i])
    v9.append(vtemp)
print(v9)
