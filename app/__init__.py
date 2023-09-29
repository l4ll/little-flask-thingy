#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:51:47 2023

@author: anon
"""

from flask import Flask




app = Flask(__name__)


from app import routes


