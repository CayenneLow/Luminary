class Contract:
    def __init__(self, moneyExpected, stages):
        self.stages = stages # list of percentages ordered by index
        self.moneyExpected = moneyExpected
        self.totalMoneyReceived = 0
        self.currentMoney = 0
        self.backers = 0
        self.currentStage = 0

    def addMoney(self, money, walletObj):
        self.currentMoney += money
        self.totalMoneyReceived += money
        self.stageMoneyReceived += money
        self.backers += 1
 		if self.totalMoneyReceived >= self.stages[currentStage]*self.moneyExpected:
 			self._releaseMoney(self.stages[currentStage]*self.moneyExpected, walletObj)
 			self.currentStage += 1


    def _releaseMoney(self, nRelease, walletObj):
    	self.currentMoney -= self.stages[currentStage]*self.moneyExpected
    	walletObj.addMoney(nRelease)