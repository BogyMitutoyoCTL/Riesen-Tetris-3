from random import randint
import Tetrisblock


class RandomBlock:
    def __init__(self):
        self.minimum = 0
        self.maximum = 6

    def get_random_block(self):
        R = randint(self.minimum, self.maximum)
        RndBlock = Tetrisblock.Blocklist[R]
        RndBlock.position = 0,0
        return RndBlock
