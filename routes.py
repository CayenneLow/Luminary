from flask import render_template, request, redirect, url_for, abort
from server import app
from src.blockchain import *
from src.smartContract import *
from src.wallet import *
from src.User import *

blockchain = Blockchain()
smartContract = Contract(30000,[0.2,0.5,1])
walletObj = Wallet()
idObj = User()
recentDonations = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/luminary')
def founderIndex():
    return render_template('project.html', role='founder', id=idObj,blockchain=blockchain, recentDonations=recentDonations[::-1], contract=smartContract)

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
        walletObj.spendMoney(int(amount), blockchain, transactionObj)
    return render_template('addTransaction.html', wallet = walletObj)

@app.route('/project')
def project():
    return render_template('project.html', id=idObj, role='user',blockchain=blockchain, recentDonations=recentDonations[::-1], contract=smartContract)

@app.route('/project/<id>/contribute', methods=['GET', 'POST'])
def projectContribute(id):
    if request.method == "POST":
        money = request.form['money']
        print(f'Contributed ${money}')
        smartContract.addMoney(int(money), walletObj)
        print(smartContract.currentMoney)
        print(walletObj.money)
        recentDonations.append(money)
        idObj.createTransaction(int(money))
        return redirect(url_for('project'))
    return render_template('contribute.html')

@app.route('/project/<id>/withdraw', methods=['GET', 'POST'])
def projectWithdraw(id):
    smartContract.withdrawMoney(int(id), idObj)
    print(smartContract.currentMoney)
    return redirect(url_for('project'))

@app.route('/transactions/<id>')
def transactions(id):
    # get blockchain
    return render_template('transactions.html', blockchain=blockchain)
