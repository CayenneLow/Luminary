from flask import render_template, request, redirect, url_for, abort
from server import app

@app.route('/')
def index():
    return 'Index for User'

@app.route('/founder')
def founderIndex():
    return 'Index for Founder'

@app.route('/project/<id>')
def project(id):
    return 'Project Page'

@app.route('/transactions/<id>')
def transactions(id):
    return 'Transactions page powered by blockchain'

