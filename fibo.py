#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: fibo.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 12:25:08 PM CST
# Content: 斐波那契数列模块

def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b

fibo(10)



def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:       
        print(b, end=' ')        
        a, b = b, a+b     
        print()  
            
def fib2(n): 
    #return Fibonacci series up to n     
    result = []     
    a, b = 0, 1     
    while b < n:
        result.append(b)         
        a, b = b, a+b     
    return result

fib(10)
list = fib2(10)
print(list)
