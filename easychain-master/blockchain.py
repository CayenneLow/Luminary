import hashlib
import time


# TODO: Sender digitally signs payload. (and recipient too?)
class Transaction:

    def __init__(self, category, amount=None , sender=None, receiver=None):
        self.size = len(category.encode('utf-8'))   # length in bytes
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f'Transaction: from: {self.sender} to: {self.receiver} amount: {str(self.amount)} category:{self.category}'



# TODO: Block creator digitally signs the block to seal it.
class Block:

    def __init__(self, transactionObj):
        self.transaction = transactionObj
        self.timestamp = None
        self.prev_hash = None
        self.hash = None

    def __get_block_hash(self):
        return hashlib.sha256(bytearray(str(self.prev_hash) + str(self.timestamp) + str(self.transaction.amount), "utf-8")).hexdigest()

    def seal(self):
        self.timestamp = time.time()
        self.hash = self.__get_block_hash()

    def __repr__(self):
        return 'Block<hash: {}, prev_hash: {}, transactions: {}, time: {}>'.format(
            self.hash, self.prev_hash, self.transaction, self.timestamp
        )



class Blockchain:

    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        if len(self.blocks) > 0:
            block.prev_hash = self.blocks[-1].hash
        block.seal()
        self.blocks.append(block)

    # Validates each block, in order.
    # An invalid block invalidates the whole chain. (well, from that point forward anyway)
    def validate(self):
        for i, block in enumerate(self.blocks):
            if i != 0 and block.prev_hash != self.blocks[i-1].hash:
                # not a genesis block
                raise InvalidBlockchain("Invalid blockchain at block {}".format(i))

    def __repr__(self):
        str = ''
        for block in self.blocks:
            str += block.__repr__()
            str += '\n\n'
        return str

class InvalidBlockchain(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
