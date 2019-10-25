import time

import Playground
import RandomBlock
import Tetrisblock
import Ws2812Painter
from LED_Matrix_Maler import Painter


class Startmenu:
    def __init__(self, playground):
        self.playground = playground
        self.playground.clear()

        square = Tetrisblock.T
        square.orientation = 2
        square.position = (1, 3)
        self.playground.put_block(square)

        square = Tetrisblock.Zr
        square.orientation = 0
        square.position = (4, 1)
        self.playground.put_block(square)

        square = Tetrisblock.L
        square.orientation = 3
        square.position = (6, 5)
        self.playground.put_block(square)

        square = Tetrisblock.I
        square.position = (1, 12)
        square.orientation = 3
        self.playground.put_block(square)

        square = Tetrisblock.Lr
        square.position = (1, 15)
        square.orientation = 2
        self.playground.put_block(square)

        square = Tetrisblock.B
        square.position = (7, 14)
        square.orientation = 0
        self.playground.put_block(square)

        square = Tetrisblock.Z
        square.position = (5, 16)
        square.orientation = 0
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

        Leonardo = Painter()
        Leonardo.write_text("* START")


if __name__ == "__main__":
    painter = Ws2812Painter.Ws2812Painter()
    playground = Playground.Playground(10, 20)
    s = Startmenu(playground)
    painter.paint(playground)
    time.sleep(100000)
