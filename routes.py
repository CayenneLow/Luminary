from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *
from src.smartContract import *
from src.wallet import *

blockchain = Blockchain()
smartContract = Contract(30000,[0.2,0.5,1])
walletObj = Wallet()

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

@app.route('/project/')
def project():
    return render_template('project.html')

@app.route('/project/contribute', methods=['GET', 'POST'])
def projectContribute():
    if request.method == "POST":
        money = request.form['money']
        print(f'Contributed ${money}')
        smartContract.addMoney(int(money), walletObj)
        print(smartContract.currentMoney)
        print(walletObj.money)
        return redirect(url_for('project'))
    return render_template('contribute.html')

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    return render_template('transactions.html', blockchain=blockchain)
