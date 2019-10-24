from random import randint
import Tetrisblock


class RandomBlock:
    def __init__(self):
        self.minimum = 0
        self.maximum = 6

    def get_random_block(self):
        R = randint(self.minimum, self.maximum)
        RndBlock = Tetrisblock.Blocklist[R]
        field=RndBlock.orientations[0]
        lines=len(field)
        RndBlock.position = 4, lines*-1
        return RndBlock
