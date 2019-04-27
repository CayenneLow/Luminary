class Contract:
    def __init__(self, releaseDate, moneyExpected):
        releaseDate = releaseDate
        moneyExpected = moneyExpected
        currentMoney = 0
        backers = 0

    def addMoney(self, money):
        self.currentMoney += money
        self.backers += 1

    def releaseMoney(self, percent, walletObj):
        decrease = self.currentMoney * percent
        self.currentMoney -= decrease
        walletObj.addMoney(decrease)

