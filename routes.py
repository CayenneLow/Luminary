from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *

blockchain = Blockchain()

@app.route('/')
def index():
    return 'Index for User'

@app.route('/founder')
def founderIndex():
    return 'Index for Founder'


@app.route('/project/addTransaction', methods=['GET', 'POST'])
def addTransaction():
    if request.method == 'POST':
        # add to blockchain function
        return render_template('addTransaction.html')
    return redirect(url_for('project', id=id))

@app.route('/project/<id>')
def project(id):
    return 'Project Page'

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    return render_template('transactions.html', blockchain=blockchain)
