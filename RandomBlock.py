from random import randint


class RandomBlock:
    def __init__(self):
        self.minimum = 1
        self.maximum = 7

    def get_random_block(self):
        return randint(self.minimum, self.maximum)




