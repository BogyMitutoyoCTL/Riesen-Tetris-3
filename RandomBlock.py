from random import randint


class RandomBlock:
    def __init__(self):
        self.minimum = 0
        self.maximum = 6

    def get_random_block(self):
        return randint(self.minimum, self.maximum)




