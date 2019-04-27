from blockchain import Block

class Wallet:
    def __init__(self):
        money = 0

    def addMoney(self, money):
        self.money += money

    def spendMoney(self, money, blockchainObj, transactionObj):
        self.money -= money
        # create Block
        block = Block(transactionObj)
        blockchainObj.add_block(block)
