from flask import render_template, request, redirect, url_for, abort
from server import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/founder')
def founderIndex():
    return 'Index for Founder'

@app.route('/founder/create', methods=['GET', 'POST'])
def founderCreate():
    if request.method == 'POST':
        # create a new blockchain for this project
        return 'created blockchain for project'
    return 'Create project for Founder'

@app.route('/founder/inputTransaction', methods=['GET', 'POST'])
def founderInput():
    if request.method == 'POST':
        # add to blockchain function
        return 'Added to blockchain'
    return 'Inputting new transaction'

@app.route('/project/<id>')
def project(id):
    return render_template('project.html', id=id)

@app.route('/project/<id>/contribute', methods=['GET', 'POST'])
def projectContribute(id):
    if request.method == "POST":
        money = request.form['money']
        print(f'Contributed ${money}')
        return redirect(url_for('project', id=id))
    return render_template('contribute.html', project=id)

@app.route('/transactions/<id>')
def transactions(id):
    return 'Transactions page powered by blockchain'

