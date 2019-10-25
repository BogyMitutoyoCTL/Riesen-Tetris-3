from random import randint
import Tetrisblock


class RandomBlock:
    def __init__(self):
        self.minimum = 0
        self.maximum = 6

    def get_random_block(self):
        R = randint(self.minimum, self.maximum)
        RndBlock = Tetrisblock.Blocklist[R]
        RndBlock.random_orientation()
        RndBlock.random_color()
        cloned_block = RndBlock.clone()
        field = RndBlock.orientations[0]
        lines = len(field)
        cloned_block.position = 4, lines * -1
        return cloned_block
