#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 05:39:38 2023

@author: anon
"""

from flask import render_template, request, redirect, g, abort
from app import app


@app.errorhandler(404)
def http_404_handler(error):
    return "<p>404 error handler works uwu</p>", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<p>500 error handler works uwu</p>", 500