class ID():
    def __init__(self):
        self.id = 0

    def createTransaction(self):
        self.id += 1
        return self.id