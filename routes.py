from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *

blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/founder')
def founderIndex():
    return 'Index for Founder'

@app.route('/project/addTransaction', methods=['GET', 'POST'])
def addTransaction():
    if request.method == 'POST':
        # add to blockchain function
        category = request.form['category'] 
        amount = request.form['amount'] 
        sender = "John"
        receiver = request.form['receiver'] 
        transactionObj = Transaction(category, amount, sender, receiver)
        print(transactionObj)
        newBlock = Block(transactionObj)
        blockchain.add_block(newBlock)
        return render_template('addTransaction.html')
    return render_template('addTransaction.html')

@app.route('/project/<id>')
def project(id):
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    B2 = Block(Transaction("Supplies", 100, "Chloe", "Collins"))
    blockchain.add_block(B2)
    return render_template('project.html', id=id, blockchain=blockchain)

@app.route('/project/<id>/contribute', methods=['GET', 'POST'])
def projectContribute(id):
    if request.method == "POST":
        money = request.form['money']
        print(f'Contributed ${money}')
        return redirect(url_for('project', id=id))
    return render_template('contribute.html', project=id)

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    return render_template('transactions.html', blockchain=blockchain)
