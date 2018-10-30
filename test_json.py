#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_json.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 05:47:21 PM CST
# Content: 
import json

d = {'name' : 'Bob', 'age' : 20, 'score' : 89}
print(json.dumps(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {
            'name' : stu.name,
            'age' : stu.age,
            'score' : stu.score
            }

s = Student('Bob', 20, 89)
print(json.dumps(s, default = student2dict))
#因为通常class的实例都有一个__dict__属性，它就是一个dict，
#用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default = lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age" : 20, "name" : "Jack", "score" : 90}'
print(json.loads(json_str, object_hook = dict2student))
