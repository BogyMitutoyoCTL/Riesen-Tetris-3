from random import randint
import Blöcke

class RandomBlock:
    def __init__(self):
        self.minimum = 0
        self.maximum = 6

    def get_random_block(self):
        R=randint(self.minimum, self.maximum)
        RndBlock= Blöcke.Blocklist[R]
        return RndBlock

Objekt=RandomBlock()
RndBlock=Objekt.get_random_block()
block_for_testing =RndBlock
for Test in range(0,11):
    block_for_testing.turnright()
    block_for_testing.showme()