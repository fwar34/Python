#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# File Name: app2.py
# Author: Feng
# Created Time: Wed Apr  3 22:34:40 2019
# Content: 

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', message = "Bad username or password", username = username)

if __name__ == '__main__':
    app.run()
