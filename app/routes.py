#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:50:38 2023

@author: anon
"""


from flask import render_template, request, redirect
from app import app



@app.route("/")
@app.route('/index')
def home_view():
    user="rabbit"
    return render_template("index.html", titlevar='home', user=user,
                           ip = request.remote_addr,
                           useragent = request.user_agent)


@app.route("/stuff")
def stuff_view():
    user="rabbit"
    return render_template("stuff.html", titlevar='stuff', user=user)


@app.route("/blog")
def blog_view():
    user="rabbit"
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template("blog.html", titlevar='blog', user=user, posts=posts)


#this thing is for testing dynamic urls
@app.route("/stuff/<int:num>/")
def stuff_num(num):
    user="rabbit"
    return render_template("stuff.html", titlevar='stuff', user=user, num=num)


@app.route('/omsk-omsk')
def nesbezhatisomska():
    return redirect("/")