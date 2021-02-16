from hashlib import sha256


def update_hash(*args):
    hashing_text = "".join([str(x) for x in args])
    h = sha256()
    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()


class Block:
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return update_hash(self.previous_hash, self.number, self.data, self.nonce)

    def __str__(self):
        return str(f"Block: {self.number}\nHash: {self.hash()}\nData: {self.data}\nNonce: {self.nonce}")


class BlockChain:
    difficulty = 3

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append({"hash": block.hash(), "previous": block.previous_hash, "number": block.number, "data": block.data, "nonce": block.nonce})

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].get("hash")

        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce += 1


def main():
    blockchain = BlockChain()
    database = ["hello world", "what's up", "hello", "bye"]

    num = 0
    for data in database:
        num += 1
        block = Block(data, num)
        blockchain.mine(block)

    # print(blockcain.chain)
    for block in blockchain.chain:
        print(block)


if __name__ == "__main__":
    main()
