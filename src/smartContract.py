from src.wallet import Wallet

class Contract:
    def __init__(self, moneyExpected, stages):
        self.stages = stages # list of percentages ordered by index
        self.moneyExpected = moneyExpected
        self.totalMoneyReceived = 0
        self.currentMoney = 0
        self.backers = 0
        self.currentStage = 0
        self.wallet = Wallet()

    def withdrawMoney(self, money):
        self.currentMoney -= money

    #walletobj is founder's wallet
    def addMoney(self, money, walletObj):
        self.currentMoney += money
        self.totalMoneyReceived += money
        self.backers += 1
        if self.totalMoneyReceived >= self.stages[self.currentStage]*self.moneyExpected:
            self._releaseMoney(self.stages[self.currentStage]*self.moneyExpected, walletObj)
            self.currentStage += 1

    def _releaseMoney(self, nRelease, walletObj):
    	self.currentMoney -= self.stages[self.currentStage]*self.moneyExpected
    	walletObj.addMoney(nRelease)