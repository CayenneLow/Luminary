class Wallet:
    def __init__(self):
        money = None

    def addMoney(self,money):
        self.money += money

    def spendMoney(self, money):
        self.money -= money
