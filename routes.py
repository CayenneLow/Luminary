from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *

@app.route('/')
def index():
    return 'Index for User'

@app.route('/founder')
def founderIndex():
    return 'Index for Founder'

@app.route('/founder/create', methods=['GET', 'POST'])
    if request.method == 'POST':
        # add to blockchain function
        return 'Added to blockchain'
    return 'Create project for Founder'

@app.route('/project/<id>')
def project(id):
    return 'Project Page'

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain 
    return 'Transactions page powered by blockchain'

