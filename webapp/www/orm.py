#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# File Name: orm.py
# Author: Feng
# Created Time: 2019-04-17 18:05
# Content:
import asyncio
import logging
import aiomysql

def log(sql, args = ()):
    logging.info('SQL: %s' % sql)

async def create_pool(loop, **kwargs):
    logging.info('create database connection pool...')
    global POOL
    POOL = await aiomysql.create_pool(host = kwargs.get('host', 'localhost'),
                                      port = kwargs.get('port', 3306),
                                      user = kwargs['user'],
                                      password = kwargs['password'],
                                      db = kwargs['db'],
                                      charset = kwargs.get('charset', 'utf8'),
                                      autocommit = kwargs.get('autocommit', True),
                                      maxsize = kwargs.get('maxsize', 10),
                                      minsize = kwargs.get('maxsize', 1),
                                      loop = loop)
