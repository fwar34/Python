#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_luap1.py
# Author: Feng
# Created Time: Tue 13 Nov 2018 08:15:35 PM CST
# Content: 
import luap
from luap import LuaRuntime
lua = LuaRuntime()
print(lua.eval('1 + 1'))

lua_function = lua.eval('function(f, n) return f(n) end')
def py_add1(n):
    return n + 1

print(lua_function(py_add1, 3))

lua_code = """
function(size)
    a = {}
    b = {}
    st = os.clock()
    for i = 0, size - 1 do
        a[i] = math.random(size)
    end

    for i = 0, size - 1 do
        b[i] = math.random(size)
    end

    print("Lua init: "..(os.clock() - st))

    st = os.clock()
    for i = 0, size -1 do
        if a[i] ~= b[i] then
            a[i] = a[i] + b[i]
        end
    end
    print("Lua sum: "..(os.clock() - st))
end
"""

test = lua.eval(lua_code)
size = 5000000
test(size)
