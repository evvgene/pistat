# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from .pitemp import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='hi', temp_stat=pi_temp(), cpu_stat='20%')
