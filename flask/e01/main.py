#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: main.py
# Author: Feng
# Created Time: 2019-04-04 10:59
# Content:
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import data_base

app = Flask(__name__)

from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField("username", [validators.DataRequired()])
    age = TextField("age", [validators.DataRequired()])
    password = PasswordField("password", [validators.DataRequired()])

@app.route('/user', methods = ['GET', 'POST'])
def login():
    my_form = LoginForm(request.form)
    if request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        # if username == 'jikexueyuan' and password == '123456':
        if my_form.username.data == 'jikexueyuan' and my_form.password.data == '123456' and my_form.validate():
            return redirect("http://www.jikexueyuan.com")
        else:
            message = "Login failed"
            return render_template('index.html', message = message, form = my_form)
    return render_template('index.html', form = my_form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    my_form = LoginForm(request.form)
    if request.method == 'POST':
        data_base.add_user(my_form.username.data, my_form.age.data, my_form.password.data)
        return "Register Successfully"
    return render_template('index.html', form = my_form)

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
