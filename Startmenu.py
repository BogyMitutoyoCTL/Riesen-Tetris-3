
import time

import Playground
import Tetrisblock
import Ws2812Painter


class Startmenu:
    def __init__(self, playground):
        self.playground = playground

        square = Tetrisblock.B
        square.position = (1, 4)
        self.playground.put_block(square)

        square = Tetrisblock.Zr
        square.position = (4, 1)
        self.playground.put_block(square)

        square = Tetrisblock.L
        square.position = (6, 5)
        square.turnleft()
        self.playground.put_block(square)

        square = Tetrisblock.I
        square.position = (1, 12)
        square.turnleft()
        self.playground.put_block(square)

        square = Tetrisblock.Lr
        square.position = (1, 15)
        square.turnleft()
        square.turnleft()
        self.playground.put_block(square)

        square = Tetrisblock.T
        square.position = (6, 14)
        self.playground.put_block(square)

        square = Tetrisblock.B
        square.position = (6, 17)
        self.playground.put_block(square)

        self.playground.set_pixel(0, 8, (255, 0, 0))
        self.playground.set_pixel(0, 9, (255, 0, 0))
        self.playground.set_pixel(0, 10, (255, 0, 0))
        self.playground.set_pixel(0, 11, (255, 0, 0))
        self.playground.set_pixel(1, 8, (255, 0, 0))
        self.playground.set_pixel(1, 10, (255, 0, 0))
        self.playground.set_pixel(2, 8, (255, 0, 0))
        self.playground.set_pixel(2, 9, (255, 0, 0))
        self.playground.set_pixel(2, 10, (255, 0, 0))

        self.playground.set_pixel(3, 8, (0, 0, 255))
        self.playground.set_pixel(3, 9, (0, 0, 255))
        self.playground.set_pixel(3, 10, (0, 0, 255))
        self.playground.set_pixel(3, 11, (0, 0, 255))
        self.playground.set_pixel(4, 11, (0, 0, 255))

        self.playground.set_pixel(5, 9, (0, 255, 0))
        self.playground.set_pixel(5, 10, (0, 255, 0))
        self.playground.set_pixel(5, 11, (0, 255, 0))
        self.playground.set_pixel(6, 8, (0, 255, 0))
        self.playground.set_pixel(6, 10, (0, 255, 0))
        self.playground.set_pixel(7, 9, (0, 255, 0))
        self.playground.set_pixel(7, 10, (0, 255, 0))
        self.playground.set_pixel(7, 11, (0, 255, 0))

        self.playground.set_pixel(7, 8, (255, 255, 0))
        self.playground.set_pixel(8, 9, (255, 255, 0))
        self.playground.set_pixel(8, 10, (255, 255, 0))
        self.playground.set_pixel(8, 11, (255, 255, 0))
        self.playground.set_pixel(9, 8, (255, 255, 0))


if __name__ == "__main__":
    painter = Ws2812Painter.Ws2812Painter()
    playground = Playground.Playground(10, 20)
    s = Startmenu(playground)
    painter.paint(playground)
    time.sleep(1000)
