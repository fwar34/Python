#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: abc_test.py
# Author: Feng
# Created Time: Thu 11 Oct 2018 03:31:42 PM CST
# Content: 定义Bird为抽象基类
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

b = Bird() #报错
