from src.blockchain import Block

class Wallet:
    def __init__(self):
        self.money = 0

    def addMoney(self, money):
        self.money += money

    def spendMoney(self, money, blockchainObj, transactionObj):
        if(self.money-money < 0):
            self.money = 0
        self.money -= money
        # create Block
        block = Block(transactionObj)
        blockchainObj.add_block(block)
