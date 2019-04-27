from blockchain import Transaction, Block, Blockchain, InvalidBlockchain

blockchain = Blockchain()

B1 = Block(Transaction("Utilities", 100, 'John', 'Collins'))
blockchain.add_block(B1)
B2 = Block(Transaction("Equipment", 200, 'Johnson', 'Collinson'))
blockchain.add_block(B2)
try:
    blockchain.validate()
    print(blockchain)
except InvalidBlockchain as err:
    print(err)
