from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *
from src.smartContract import *

blockchain = Blockchain()
smartContract = Contract(12,12)

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

@app.route('/project/', methods=['GET', 'POST'])
def project():
    if request.method == 'POST':
        money = request.form['money']
        print(money)
        print(int(money))
        smartContract.addMoney(int(money))
        #print(smartContract.currentMoney)
        return render_template('project.html')
    return render_template('project.html')

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    return render_template('transactions.html', blockchain=blockchain)
