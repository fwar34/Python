#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: property_test.py
# Author: Feng
# Created Time: Thu 11 Oct 2018 02:59:42 PM CST
# Content: 

#without property
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

student = Student("Leo", 90)
print("{} score {}".format(student.name, student.get_score()))

student.set_score(100)
print("{} score {}".format(student.name, student.get_score()))

#property
class Student2:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

student2 = Student2("Leo", 90)
print("{} score {}".format(student2.name, student2.score))
student2.score = 100
print("{} score {}".format(student2.name, student2.score))
