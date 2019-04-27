from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *
from src.smartContract import *
from src.wallet import *
from src.ID import *

blockchain = Blockchain()
smartContract = Contract(30000,[0.2,0.5,1])
walletObj = Wallet()
id = ID()

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
       # print(walletObj.money)
        walletObj.spendMoney(int(amount), blockchain, transactionObj)
       # print(walletObj.money)
        return render_template('addTransaction.html')
    return render_template('addTransaction.html')

@app.route('/project')
def project():
    id.createTransaction()
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
        smartContract.addMoney(int(money), walletObj)
        print(smartContract.currentMoney)
        print(walletObj.money)
        return redirect(url_for('project'))
    return render_template('contribute.html')

@app.route('/project/<id>/withdraw', methods=['GET', 'POST'])
def projectWithdraw(id):
    if request.method == "POST":
        money = request.form['money']
        print(f'Withdrew ${money}')
        smartContract.withdrawMoney(int(money))
        print(smartContract.currentMoney)
        return redirect(url_for('project'))
    return render_template('withdraw.html')

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    B1 = Block(Transaction("Utilities", 100, "John", "Collins"))
    blockchain.add_block(B1)
    return render_template('transactions.html', blockchain=blockchain)
