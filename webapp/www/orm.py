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

async def select(sql, args, size = None):
    log(sql, args)
    global POOL
    async with POOL.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args, auto_commit = True):
    log(sql)
    async with POOL.get() as conn:
        if not auto_commit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not auto_commit:
                await conn.commit()
        except BaseException as e:
            if not auto_commit:
                await conn.rollback()
            raise
        return affected

def create_arg_string(num):
    lst = []
    for n in range(num):
        lst.append('?')
    return ', ' . join(lst)

class Field(object):

    def __init__(self, name, colum_type, primary_key, default):
        self.name = name
        self.colum_type = colum_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.colum_type, self.name)

class StringField(Field):

    def __init__(self, name = None, primary_key = False, default = None, ddl = 'varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):

    def __init__(self, name = None, default = False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):

    def __init__(self, name = None, primary_key = False, default = 0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):

    def __init__(self, name = None, primary_key = False, default = 0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):

    def __init__(self, name = None, default = None):
        super().__init__(name, 'text', False, default)

class ModeMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        table_name = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, table_name))
        mappings = dict()
        fields = []
        primar_key = None
        for k, v in attrs.item():
            if isinstance(v, Field):
                logging.info(' found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    raise StandardError('Duplicate key for field: %s' % k)
                primar_key = k
            else:
                fields.append(k)
        if not primar_key:
            raise StandardError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
