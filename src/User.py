class User():
    def __init__(self):
        self.id = 0
        self.invested = []

    def createTransaction(self, money):
        self.invested.append(int(money))
        self.id += 1
        return self.id