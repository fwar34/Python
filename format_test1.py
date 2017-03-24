#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: format_test1.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 01:31:30 PM CST
# Content: 

print('{0} and {1}, {other}'.format('aa', 'bb', other='cc'))
print('{1} and {0}, {other}'.format('aa', 'bb', other='cc'))

#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr())
#可以用于在格式化某个值之前对其进行转化
import math
print('PI is {}'.format(math.pi))
print('PI is {!r}'.format(math.pi))

#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
#下面的例子将 Pi保留到小数点后三位''
print('PI is {0:.3f}'.format(math.pi))
print('PI is {:.3f} {:.4f}'.format(math.pi, math.pi))

#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ===> {1:10}'.format(name, phone))
    print('{0:10} ===> {1:10d}'.format(name, phone))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开,
# 那么在格式化时通过变量名而非位置会是很好的事情。
#最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
print('Jack:{0[Jack]:d}; Sjoerd:{0[Sjoerd]:d}; '
        'Dcab:{0[Dcab]:d}'.format(table))

#也可以通过在 table 变量前使用 '**' 来实现相同的功能
print('Jack:{Jack:d}; Sjoerd:{Sjoerd:d}; Dcab:{Dcab:d}'.format(**table))
