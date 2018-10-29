#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: unit_test_mydict.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 10:27:12 AM CST
# Content: 
import unittest
from my_dict import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_init(self):
        d = Dict(a = 1, b = 'Test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'Test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def  test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
