#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# File Name: auth.py
# Author: Feng
# Created Time: 2019-04-13 10:10
# Content:
import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix = '/auth')

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        # 通过查询数据库，检查是否有查询结果返回来验证 username 是否已被注册。 
        # db.execute 使用了带有 ? 占位符 的 SQL 查询语句。占位符可以代替后面的元组参数中相应的值。
        # 使用占位符的 好处是会自动帮你转义输入值，以抵御 SQL 注入攻击 。
        elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone() is not None:
            error = 'User {} is already registered.' . format(username)

        # 如果验证成功，那么在数据库中插入新用户数据。为了安全原因，不能把密码明文 
        # 储存在数据库中。相代替的，使用 generate_password_hash() 生成安全的哈希值并储存 到数据库中。
        # 查询修改了数据库是的数据后使用 meth:db.commit() <sqlite3.Connection.commit> 保存修改。
        if error is None:
            db.execute('INSERT INTO user (username, password) values (?, ?)', (username, generate_password_hash(password)))
            db.commit()
            # 用户数据保存后将转到登录页面。 url_for() 根据登录视图的名称生成相应的 URL 。
            # 与写固定的 URL 相比， 这样做的好处是如果以后需要修改该视图相应的 URL ，
            # 那么不用修改所有涉及到 URL 的代码。 redirect() 为生成的 URL 生成一个重定向响应。
            return redirect(url_for('auth.login'))

        flash(error)
    return  render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')

# bp.before_app_request() 注册一个 在视图函数之前运行的函数，不论其 URL 是什么。 
# load_logged_in_user 检查用户 id 是否已经储存在 session 中，并从数据库中获取用户数据，
# 然后储存在 g.user 中。 g.user 的持续时间比请求要长。 
# 如果没有用户 id ，或者 id 不存在，那么 g.user 将会是 None 。
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()

# 注销的时候需要把用户 id 从 session 中移除。 然后 load_logged_in_user 就不会在后继请求中载入用户了。
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
